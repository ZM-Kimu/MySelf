from flask import Response, request
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

from app import auth, db
from app.models.user import User
from app.utils import (
    DEBUG_ERR_ARGUMENT,
    DEBUG_EXCEPT_INTERNAL,
    DEBUG_EXCEPT_SQL,
    ERR_INTERNAL_SERVER,
    ERR_INVALID_ARGUMENTS,
    MSG_ERR,
    return_to_server,
)


class CreateUser(Resource):
    @auth.login_required
    def post(self) -> Response:
        try:
            data = request.get_json()
            name = data.get("name")
            age = data.get("age")
            gender = data.get("gender")

            if not all([name, age, gender]):
                return return_to_server(
                    MSG_ERR, ERR_INVALID_ARGUMENTS, DEBUG_ERR_ARGUMENT
                )

            user = User(name=name, age=age, gender=gender)
            db.session.add(user)
            db.session.commit()

            return return_to_server(data={"user_uuid": user.uuid})
        except SQLAlchemyError as e:
            db.session.rollback()
            return return_to_server(MSG_ERR, ERR_INTERNAL_SERVER, DEBUG_EXCEPT_SQL + e)
        except Exception as e:
            return return_to_server(
                MSG_ERR, ERR_INTERNAL_SERVER, DEBUG_EXCEPT_INTERNAL + str(e)
            )
