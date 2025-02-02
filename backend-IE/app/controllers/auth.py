from uuid import uuid4

from flask import Response, request
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash, generate_password_hash

from app import auth, db
from app.models.admin import Admin
from app.utils import (
    DEBUG_CONDITION_NOT_MATCH,
    DEBUG_CONFLICTION,
    DEBUG_ERR_ARGUMENT,
    DEBUG_ERR_REACH_END,
    DEBUG_EXCEPT_INTERNAL,
    DEBUG_EXCEPT_SQL,
    ERR_AUTH_FAILED,
    ERR_CONFLICTION,
    ERR_INTERNAL_SERVER,
    ERR_INVALID_ARGUMENTS,
    MSG_AUTH_ERR,
    MSG_ERR,
    return_to_server,
)

tokens = {}


@auth.verify_token
def verify_token(token) -> str | None:
    if token in tokens:
        return tokens[token]
    return None


class Login(Resource):
    def post(self) -> Response:
        try:
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")
            if not username or not password:
                return return_to_server(
                    MSG_ERR, ERR_INVALID_ARGUMENTS, DEBUG_ERR_ARGUMENT
                )
            admin = Admin.query.filter_by(username=username).first()
            if admin and check_password_hash(admin.password, password):
                token = str(uuid4())
                tokens[token] = admin.role
                return return_to_server(data={"token": token})
            return return_to_server(
                MSG_AUTH_ERR, ERR_INVALID_ARGUMENTS, DEBUG_ERR_REACH_END
            )
        except Exception as e:
            return return_to_server(
                MSG_ERR, ERR_INTERNAL_SERVER, DEBUG_EXCEPT_INTERNAL + str(e)
            )


class SignupAdmin(Resource):
    @auth.login_required
    def post(self) -> Response:
        try:
            current_role = tokens.get(auth.current_user())
            if current_role != "super":
                return return_to_server(
                    MSG_AUTH_ERR, ERR_AUTH_FAILED, DEBUG_CONDITION_NOT_MATCH
                )
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")
            role = data.get("role")

            if not all([username, password, role]):
                return return_to_server(
                    MSG_ERR, ERR_INVALID_ARGUMENTS, DEBUG_ERR_ARGUMENT
                )

            if Admin.query.filter_by(username=username).first():
                return return_to_server(MSG_ERR, ERR_CONFLICTION, DEBUG_CONFLICTION)

            new_admin = Admin(
                username=username, password=generate_password_hash(password), role=role
            )
            db.session.add(new_admin)
            db.session.commit()
            return return_to_server()
        except SQLAlchemyError as e:
            db.session.rollback()
            return return_to_server(MSG_ERR, ERR_INTERNAL_SERVER, DEBUG_EXCEPT_SQL + e)
        except Exception as e:
            return return_to_server(
                MSG_ERR, ERR_INTERNAL_SERVER, DEBUG_EXCEPT_INTERNAL + str(e)
            )
