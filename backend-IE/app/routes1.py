import base64
import logging
import os
from uuid import uuid4

from flask import Response, request, send_file
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash, generate_password_hash

from app import api, app, auth, db
from app.models import IEAdmin, IEConversation, IEUser


class GetImage(Resource):
    @auth.login_required
    def get(self, conversation_uuid: str) -> Response:
        try:
            image_path = os.path.join(
                app.root_path, app.config.get("IMAGE_PATH"), f"{conversation_uuid}.jpg"
            )
            if not os.path.exists(image_path):
                return return_to_server(MSG_ERR, ERR_NOT_FOUND, DEBUG_NOT_FOUND)
            return send_file(image_path, mimetype="image/jpeg")
        except Exception as e:
            return return_to_server(
                MSG_ERR, ERR_INTERNAL_SERVER, DEBUG_EXCEPT_INTERNAL + str(e)
            )


api.add_resource(GetImage, "/img/<string:conversation_uuid>")
