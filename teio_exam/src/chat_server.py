import socket
import threading
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.chat_window import ChatWindow


class ChatServer:
    MAIN_SERVER = "0.0.0.0"
    BACKUP_SERVER = "0.0.0.0"
    PUB_SERVER = "0.0.0.0"
    COM_PORT = 19198

    def __init__(self, chat_window: "ChatWindow") -> None:
        self.sock: Optional[socket.socket] = None
        self.chat_window = chat_window
        self.connected = False
        self.running = True
        self.current_server_ip = ""
        self.chat_history: list[str] = []

    def connect(self) -> str:
        """连接到聊天服务器"""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = ""
        failed = False

        servers = [
            (self.MAIN_SERVER, "✅ 已连接主服务器"),
            (self.BACKUP_SERVER, "✅ 已连接备用服务器"),
            (self.PUB_SERVER, "✅ 已连接公有服务器"),
        ]

        for server_ip, success_msg in servers:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.settimeout(1)
                self.sock.connect((server_ip, self.COM_PORT))
                self.current_server_ip = server_ip
                result = success_msg
                break
            except Exception as e:
                if server_ip == self.PUB_SERVER and self.sock:
                    self.sock.close()
                    self.sock = None
                    failed = True
                    result = f"❌ 服务器连接失败，请重新进入：{e}"

        if not failed:
            self.connected = True
            threading.Thread(target=self.receiver, daemon=True).start()

        return result

    def receiver(self) -> None:
        """接收消息的线程"""
        while self.running:
            try:
                if self.sock is None:
                    continue
                msg = self.sock.recv(8192)
                if not msg:
                    continue
                self.chat_history.append(msg.decode("utf-8", "surrogatepass"))
            except:
                continue

    def send(self, msg: str, dont_append: bool = False) -> None:
        """发送消息"""
        if self.sock:
            self.sock.sendall(msg.encode("utf-8", "surrogatepass"))
            if not dont_append:
                self.chat_history.append(msg)

    def current_ip(self) -> str:
        """获取当前连接的IP"""
        if self.sock is None:
            return ""
        return self.sock.getsockname()[0]

    def close(self) -> None:
        """关闭连接"""
        self.running = False
        try:
            if self.sock:
                self.sock.shutdown(socket.SHUT_RDWR)
                self.sock.close()
        except:
            pass
