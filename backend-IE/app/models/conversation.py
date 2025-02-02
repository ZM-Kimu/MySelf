import uuid

from app import db


class Conversation(db.Model):
    __tablename__ = "conversations"
    uuid = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_uuid = db.Column(db.String(36), db.ForeignKey("user.uuid"), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    type = db.Column(db.String(20), nullable=False)
    question = db.Column(db.String(1536), nullable=False)  # 512个汉字
    answer = db.Column(db.String(12288), nullable=True)  # 4096个汉字
    prompt = db.Column(db.String(1536), nullable=True)  # 512个汉字
    image = db.Column(db.Text, nullable=True)
    is_processed = db.Column(db.Boolean, nullable=False, default=False)
