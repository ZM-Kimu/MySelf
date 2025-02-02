from app import api
from app.controllers.user import CreateUser

api.add_resource(CreateUser, "/create_user")
