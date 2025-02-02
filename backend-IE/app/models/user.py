import uuid

from app import db


class User(db.Model):
    __tablename__ = "users"
    uuid = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(16), nullable=False)
