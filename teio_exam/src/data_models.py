from dataclasses import dataclass
from typing import Optional


@dataclass
class DocData:
    file_name: str
    questions: str


@dataclass
class ChatMessage:
    content: str
    timestamp: str
    sender_ip: str
    nickname: Optional[str] = None
    is_admin: bool = False
