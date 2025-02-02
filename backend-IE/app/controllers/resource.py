import os

from flask import Response, send_file
from flask_restful import Resource

from app import app, auth
from app.utils import (
    DEBUG_EXCEPT_INTERNAL,
    DEBUG_NOT_FOUND,
    ERR_INTERNAL_SERVER,
    ERR_NOT_FOUND,
    MSG_ERR,
    return_to_server,
)


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
