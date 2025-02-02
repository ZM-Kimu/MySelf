from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config.from_object("config.Config")

db = SQLAlchemy(app)
api = Api(app)
auth = HTTPTokenAuth()

from app.models import admin, conversation, user
from app.routes import conversation, user
