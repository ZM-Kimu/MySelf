import datetime
from typing import Optional

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from src.chat_server import ChatServer
from src.file_reader import FileReader


class ChatWindow(QWidget):
    def __init__(self, parent: QWidget, admin: bool = False) -> None:
        super().__init__(parent)

        self.admin = admin
        self.nickname = ""
        self.input_text = ""
        self.last_history_index = 0
        self.server: Optional[ChatServer] = None
        self.top_layout: QHBoxLayout

        self.init_window()
        self.init_ui()

    def init_window(self) -> None:
        """初始化窗口属性"""
        self.setFixedSize(190, 190)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.Window)
        self.setWindowIcon(QIcon(FileReader.resource_path("./data/icon.ico")))
        self.setWindowTitle("聊天室")

    def init_ui(self) -> None:
        """初始化用户界面"""
        layout = QVBoxLayout()

        # 顶部控制区域
        self.top_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.rename_button = QPushButton("改名")
        self.kick_button = QPushButton("踢")
        self.kick_button.setFixedWidth(30)

        self.top_layout.addWidget(self.name_input)
        self.top_layout.addWidget(self.rename_button)
        self.top_layout.addWidget(self.kick_button)

        self.name_input.setPlaceholderText("昵称")
        self.rename_button.clicked.connect(self.rename_username)
        self.kick_button.clicked.connect(self.kick_ip)
        layout.addLayout(self.top_layout)

        # 聊天区域
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        layout.addWidget(self.chat_area)

        # 输入区域
        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("对话...[Enter发送]")
        self.input_line.returnPressed.connect(self.send_message)
        layout.addWidget(self.input_line)

        layout.setSpacing(1)
        layout.setContentsMargins(3, 3, 3, 3)
        self.setLayout(layout)

        # 启动定时器同步聊天历史
        self.timer = QTimer()
        self.timer.timeout.connect(self.sync_history_to_ui)
        self.timer.start(200)

    def update_layout(self) -> None:
        """根据管理员权限更新布局"""
        self.kick_button.setVisible(self.admin)
        self.update()

    def connect_to_server(self) -> str:
        """连接到聊天服务器"""
        if self.server is None:
            self.server = ChatServer(self)

        if not self.server.connected:
            result = self.server.connect()
            self.append_to_chat_area(result)

            if self.server.connected:
                # 发送加入消息
                join_msg = f"[{self.server.current_ip()}]{'[📍管理员📍]' if self.admin else ''} 加入了网络聊天室🆗"
                self.server.send(join_msg, dont_append=True)

            return result

        return "已连接"

    def formatted_time(self) -> str:
        """格式化当前时间"""
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")

    def rename_username(self) -> None:
        """重命名用户名"""
        text = self.name_input.text().strip()
        if text:
            self.nickname = text
            self.append_to_chat_area(f"[系统] 昵称修改为：{self.nickname}")

    def append_to_chat_area(self, text: str) -> None:
        """向聊天区域添加文本"""
        self.chat_area.append(text)

    def send_message(self) -> None:
        """发送消息"""
        try:
            text = self.input_line.text().strip()
            if not text or not self.server or not self.server.connected:
                return

            self.input_line.clear()
            admin_prefix = "[📍管理员📍]" if self.admin else ""
            nickname_suffix = f"[{self.nickname}]" if self.nickname else ""

            msg = f"[{self.formatted_time()}]{admin_prefix}[{self.server.current_ip()}]{nickname_suffix}:\n{text}"
            self.server.send(msg)

        except Exception:
            # 如果发送失败，尝试重新连接
            if self.server:
                self.server.connect()
            self.input_line.setText(text)
            self.send_message()

    def kick_ip(self) -> None:
        """踢出指定IP（管理员功能）"""
        if not self.admin:
            return

        text = self.input_line.text().strip()
        if self.server and self.server.connected and text:
            self.input_line.clear()
            self.server.send(f"1919/kick {text}", dont_append=True)

    def sync_history_to_ui(self) -> None:
        """同步聊天历史到UI"""
        if not self.server:
            return

        new_items = self.server.chat_history[self.last_history_index :]
        for line in new_items:
            self.chat_area.append(line)
        self.last_history_index += len(new_items)

    def set_admin_status(self, is_admin: bool) -> None:
        """设置管理员状态"""
        self.admin = is_admin
        self.update_layout()

    def get_server_ip(self) -> str:
        """获取当前服务器IP"""
        if self.server:
            return self.server.current_server_ip
        return ""

    def closeEvent(self, event: QCloseEvent) -> None:
        """窗口关闭事件"""
        if self.server:
            self.server.close()
        if self.timer.isActive():
            self.timer.stop()
        super().closeEvent(event)
