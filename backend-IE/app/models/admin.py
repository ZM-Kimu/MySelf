import uuid

from app import db


class Admin(db.Model):
    __tablename__ = "admin"
    uuid = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(16), nullable=False)  # super, normal, base
