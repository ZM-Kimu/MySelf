import base64
import os
from uuid import uuid4

from flask import Response, request
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

from app import api, app, auth, db
from app.models.conversation import Conversation
from app.models.user import User
from app.utils import (
    DEBUG_ERR_ARGUMENT,
    DEBUG_EXCEPT_INTERNAL,
    DEBUG_EXCEPT_SQL,
    DEBUG_NOT_FOUND,
    ERR_INTERNAL_SERVER,
    ERR_INVALID_ARGUMENTS,
    ERR_NOT_FOUND,
    MSG_ERR,
    return_to_server,
)


class CreateConversation(Resource):
    @auth.login_required
    def post(self) -> Response:
        try:
            data = request.get_json()
            user_uuid = data.get("user_uuid")
            question = data.get("question")
            answer = data.get("answer")
            prompt = data.get("prompt")
            type = data.get("type")
            image = data.get("image")

            if not all([user_uuid, question, answer, prompt, type, image]):
                return return_to_server(
                    MSG_ERR, ERR_INVALID_ARGUMENTS, DEBUG_ERR_ARGUMENT
                )
            if not User.query.filter_by(uuid=user_uuid).first():
                return return_to_server(MSG_ERR, ERR_NOT_FOUND, DEBUG_NOT_FOUND)

            conversation = Conversation(
                user_uuid=user_uuid,
                question=question,
                answer=answer,
                prompt=prompt,
                type=type,
            )
            db.session.add(conversation)
            db.session.commit()

            image_data = base64.b64decode(image)
            image_path = os.path.join(
                app.root_path, app.config.get("IMAGE_PATH"), f"{conversation.uuid}.jpg"
            )
            with open(image_path, "wb") as f:
                f.write(image_data)

            return return_to_server(data={"conversation_uuid": conversation.uuid})
        except SQLAlchemyError as e:
            db.session.rollback()
            return return_to_server(MSG_ERR, ERR_INTERNAL_SERVER, DEBUG_EXCEPT_SQL + e)
        except Exception as e:
            return return_to_server(
                MSG_ERR, ERR_INTERNAL_SERVER, DEBUG_EXCEPT_INTERNAL + str(e)
            )


class DeleteConversation(Resource):
    @auth.login_required
    def delete(self, conversation_uuid) -> Response:
        try:
            conversation = Conversation.query.filter_by(uuid=conversation_uuid).first()
            if not conversation:
                return return_to_server(MSG_ERR, ERR_NOT_FOUND, DEBUG_NOT_FOUND)

            db.session.delete(conversation)
            db.session.commit()

            return return_to_server()
        except SQLAlchemyError as e:
            db.session.rollback()
            return return_to_server(MSG_ERR, ERR_INTERNAL_SERVER, DEBUG_EXCEPT_SQL + e)
        except Exception as e:
            return return_to_server(
                MSG_ERR, ERR_INTERNAL_SERVER, DEBUG_EXCEPT_INTERNAL + str(e)
            )


class GetConversations(Resource):
    @auth.login_required
    def post(self) -> Response:
        try:
            data = request.get_json(silent=True) or {}
            start = data.get("start", 0)
            count = data.get("count", 10e10)
            total_count = Conversation.query.count()
            start = min(start, total_count - 1)
            count = min(count, total_count)

            conversations = (
                db.session.query(Conversation, User)
                .join(User, Conversation.user_uuid == User.uuid)
                .offset(start)
                .limit(count)
                .all()
            )
            result = [
                {
                    "uuid": conv.uuid,
                    "user_uuid": user.uuid,
                    "user_age": user.age,
                    "is_processed": conv.is_processed,
                    "time": conv.time.isoformat(),
                    "question": {
                        "type": conv.type,
                        "content": conv.question,
                        "answer": conv.answer,
                        "prompt": conv.prompt,
                        "image": f"/img/{conv.uuid}",
                    },
                }
                for conv, user in conversations
            ]
            return return_to_server(data=result)
        except SQLAlchemyError as e:
            db.session.rollback()
            return return_to_server(MSG_ERR, ERR_INTERNAL_SERVER, DEBUG_EXCEPT_SQL + e)
        except Exception as e:
            return return_to_server(
                MSG_ERR, ERR_INTERNAL_SERVER, DEBUG_EXCEPT_INTERNAL + str(e)
            )
