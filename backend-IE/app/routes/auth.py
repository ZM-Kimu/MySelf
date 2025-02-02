from app import api
from app.controllers.auth import Login, SignupAdmin

api.add_resource(Login, "/login")
api.add_resource(SignupAdmin, "/signup_admin")
