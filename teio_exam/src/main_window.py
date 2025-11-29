import sys
import threading
import time

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QMoveEvent
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)

from src.api_client import ApiClient
from src.chat_window import ChatWindow
from src.data_models import DocData
from src.file_reader import FileReader
from src.image_processor import ImageProcessor
from src.input_monitor import ClipboardMonitor, MouseSequenceListener
from src.resizable_frameless_window import ResizableFramelessWindow
from src.search_engine import SearchEngine
from src.utils import AppConstants
from src.window_manager import EventBridge, MouseEventHandler, TopmostWidget


class MainWindow(ResizableFramelessWindow):
    def __init__(self) -> None:
        super().__init__()

        # 基础属性
        self.confirm_exit = False
        self.docs_data: list[DocData] = []
        self.current_doc_index: int = 0
        self.current_position_map: dict[int, int] = {}
        self.last_search_keyword: str = ""

        # 组件初始化
        self.init_window()
        self.init_ui()
        self.init_components()
        self.init_controller()

        # 启动功能
        self.setup_initial_state()

    def init_window(self) -> None:
        """初始化窗口属性"""
        # self.setFixedSize(210, 190)
        self.setMinimumSize(210, 190)
        self.resize(210, 190)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        self.setWindowIcon(QIcon(FileReader.resource_path("./data/icon.ico")))
        self.setWindowTitle(AppConstants.APP_TITLE)

    def init_ui(self) -> None:
        """初始化用户界面"""
        layout = QVBoxLayout()

        # 结果显示
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        self.result_area.setPlainText(AppConstants.WELCOME_TEXT)
        layout.addWidget(self.result_area, stretch=5)

        # 搜索输入
        input_layout = QHBoxLayout()
        self.keyword_input = QLineEdit()
        self.keyword_input.setPlaceholderText("输入关键字或代号")
        self.keyword_input.returnPressed.connect(self._smart_search)

        # 搜索状态
        self.search_status_label = QLabel("")
        self.search_status_label.setFixedWidth(35)
        self.search_status_label.setStyleSheet("color: gray; font-size: 10px;")

        self.regex_search_button = QPushButton("正则搜")
        self.search_button = QPushButton("检索")

        self.regex_search_button.setFixedWidth(65)
        self.search_button.setFixedWidth(35)

        self.search_button.clicked.connect(lambda: self._perform_search(False))
        self.regex_search_button.clicked.connect(lambda: self._perform_search(True))

        input_layout.addWidget(self.keyword_input)
        input_layout.addWidget(self.search_status_label)
        input_layout.addWidget(self.regex_search_button)
        input_layout.addWidget(self.search_button)
        layout.addLayout(input_layout)

        # 题库切换区域
        subject_layout = QHBoxLayout()
        self.switch_subject_button = QPushButton("获取题目")
        self.doc_status_label = QLabel("0/0")
        self.doc_status_label.setFixedWidth(35)

        self.switch_subject_button.clicked.connect(self.switch_next_doc)

        subject_layout.addWidget(self.switch_subject_button)
        subject_layout.addWidget(self.doc_status_label)
        layout.addLayout(subject_layout)

        # 功能按钮区域
        self.chatroom_button = QPushButton("猴子")
        self.exit_button = QPushButton("关闭")

        self.chatroom_button.clicked.connect(self.toggle_chat_window)
        self.exit_button.clicked.connect(self.exit_confirm)

        layout.addWidget(self.chatroom_button)
        layout.addWidget(self.exit_button)

        # 设置布局
        layout.setSpacing(1)
        layout.setContentsMargins(3, 3, 3, 3)
        self.setLayout(layout)

    def init_components(self) -> None:
        """初始化各个组件"""
        self.chat_window = ChatWindow(self)
        self.controller_bridge = EventBridge()
        self.topmost_widget = TopmostWidget(self)
        self.clipboard_monitor = ClipboardMonitor(self, self.clipboard_search)
        self.mouse_action = MouseSequenceListener()
        # self.ocr_capture_manager = OCRCaptureManager()
        self.api_client = ApiClient()
        self.search_engine = SearchEngine()
        self.image_processor = ImageProcessor()

    def init_controller(self) -> None:
        """初始化控制器和事件绑定"""
        # 绑定事件信号
        self.controller_bridge.right_click_move_signal.connect(
            MouseEventHandler.move_window_position
        )
        self.controller_bridge.middle_click_topmost_signal.connect(
            MouseEventHandler.toggle_topmost
        )
        self.controller_bridge.toggle_show_hidd_signal.connect(
            self.toggle_main_and_chat_hiding
        )
        self.controller_bridge.toggle_pure_mode.connect(self.toggle_pure_mode)

        # 绑定鼠标手势
        self.mouse_action.uuddllrr_match_signal.connect(
            self.controller_bridge.toggle_show_hidd_signal.emit
        )
        self.mouse_action.udud_match_signal.connect(
            self.controller_bridge.toggle_pure_mode.emit
        )

        self.search_engine.search_status_updated.connect(self.update_search_status)
        # self.ocr_capture_manager.text_recognized.connect(self.handle_ocr_result)
        # self.mouse_action.udlr_match_signal.connect(self.trigger_ocr_capture)

        # 设置全局鼠标监听
        MouseEventHandler.setup_global_mouse_listener(self.controller_bridge, self)

    def setup_initial_state(self) -> None:
        """设置初始状态"""
        self.topmost_widget.enable = False

        # 初始化聊天窗口（但不显示）
        self.toggle_chat_window(func_call=True)
        self.toggle_chat_window()

        # 隐藏主界面
        # self.toggle_main_and_chat_hiding()

        # 启动置顶监控
        QTimer.singleShot(400, self.topmost_widget.enforce_topmost_forever)
        self.chat_window.hide()

    def moveEvent(self, event: QMoveEvent) -> None:
        """窗口移动事件，同步聊天窗口位置"""
        super().moveEvent(event)
        if self.chat_window and self.chat_window.isVisible():
            self.chat_window.move(self.x() + self.width(), self.y())

    def clipboard_search(self, text: str) -> None:
        """剪贴板搜索回调"""
        self.keyword_input.setText(text)
        self._perform_search(False)

    def load_docs_from_server(self) -> None:
        """从服务器加载文档数据"""
        try:
            server_ip = self.chat_window.get_server_ip()
            if not server_ip:
                self.result_area.setPlainText("⚠️ 未能连接到服务器")
                return

            self.api_client.host = server_ip
            self.docs_data = self.api_client.fetch_questions()

            if self.docs_data:
                self.current_doc_index = 0
                self.update_doc_display()
            else:
                self.result_area.setPlainText("⚠️ 未获取到题目数据")

        except Exception as e:
            self.result_area.setPlainText(f"❌ 拉取题目失败：{str(e)}")

    def update_doc_display(self) -> None:
        """更新文档显示"""
        if not self.docs_data:
            self.switch_subject_button.setText("获取题目")
            self.doc_status_label.setText("0/0")
            self.current_position_map = {}
            return

        if 0 <= self.current_doc_index < len(self.docs_data):
            current_doc = self.docs_data[self.current_doc_index]

            _, position_map = self.image_processor.insert_images_into_textarea(
                self.result_area, current_doc.questions
            )
            self.current_position_map = position_map

            self.switch_subject_button.setText(current_doc.file_name)

            self.doc_status_label.setText(
                f"{self.current_doc_index + 1}/{len(self.docs_data)}"
            )

            self.search_engine.clear_search()
            self.search_status_label.setText("")
        else:
            self.result_area.setPlainText("❌ 文档索引超出范围")
            self.doc_status_label.setText("0/0")
            self.current_position_map = {}

    def switch_next_doc(self) -> None:
        """切换到下一个文档"""
        if not self.docs_data:
            self.load_docs_from_server()
            return

        self.current_doc_index = (self.current_doc_index + 1) % len(self.docs_data)
        self.update_doc_display()

    def _perform_search(self, use_regex: bool) -> None:
        """执行搜索操作"""
        keyword = self.keyword_input.text().strip()
        self.last_search_keyword = keyword

        if not keyword:
            self.search_engine.clear_search()
            self.search_status_label.setText("")
            return

        if not self.docs_data:
            self.result_area.setPlainText("❌ 没有可搜索的题库数据")
            self.search_status_label.setText("0/0")
            return

        current_doc = self.docs_data[self.current_doc_index]

        search_text = ImageProcessor.get_text_only_for_search(current_doc.questions)

        match_count = self.search_engine.highlight_text_in_textarea(
            self.result_area, search_text, keyword, use_regex
        )

        if match_count == 0:
            self.search_status_label.setText("0/0")

    def _smart_search(self) -> None:
        """智能搜索：如果关键字相同则切换到下一个匹配项，否则执行新搜索"""
        current_keyword = self.keyword_input.text().strip()

        if current_keyword == self.last_search_keyword and current_keyword:
            self.search_engine.find_next()
        else:
            self.last_search_keyword = current_keyword
            self._perform_search(False)

    def _find_normal_matches_in_text(
        self, text: str, keyword: str
    ) -> list[tuple[int, int]]:
        """在文本中查找普通匹配"""
        matches = []
        keyword_lower = keyword.lower()
        text_lower = text.lower()
        start = 0

        while True:
            pos = text_lower.find(keyword_lower, start)
            if pos == -1:
                break
            matches.append((pos, pos + len(keyword)))
            start = pos + 1

        return matches

    def update_search_status(self, current_index: int, total_matches: int) -> None:
        """更新搜索状态显示"""
        if total_matches > 0:
            self.search_status_label.setText(f"{current_index}/{total_matches}")
        else:
            self.search_status_label.setText("0/0")

    # def trigger_ocr_capture(self):
    # """触发OCR截图"""
    # if self.ocr_capture_manager.is_ocr_ready():
    # self.ocr_capture_manager.start_capture()
    # else:
    # self.result_area.setPlainText("⚠️ OCR引擎未初始化完毕，请稍后再试")

    # def handle_ocr_result(self, text: str):
    #     """处理OCR识别结果"""
    #     if text.strip():
    #         self.keyword_input.setText(text.strip())
    #         self._perform_search(False)

    def toggle_main_and_chat_hiding(self) -> None:
        """切换主窗口和聊天窗口的显示/隐藏状态"""

        def _do() -> None:
            if self.isVisible():
                self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
                self.hide()
                if self.chat_window:
                    self.chat_window.hide()
                self.topmost_widget.enable = False
            else:
                self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
                self.show()
                self.topmost_widget.enable = True
            self.repaint()

        QTimer.singleShot(0, _do)

    def toggle_pure_mode(self) -> None:
        """切换纯净模式"""
        is_visible = self.exit_button.isVisible()

        if is_visible:
            self.setMinimumSize(210, 85)
            self.resize(210, 85)
        else:
            self.setMinimumSize(210, 190)
            if self.height() < 190:
                self.resize(self.width(), 190)

        widgets_to_toggle = [
            # self.keyword_input,
            # self.search_status_label,
            # self.regex_search_button,
            # self.search_button,
            self.switch_subject_button,
            self.doc_status_label,
            self.chatroom_button,
            self.exit_button,
        ]

        for widget in widgets_to_toggle:
            widget.setVisible(not is_visible)

        self.layout().update()
        self.layout().activate()

    def toggle_chat_window(self, func_call: bool = False) -> None:
        """切换聊天窗口的显示状态"""
        if self.chat_window.isVisible():
            self.chat_window.hide()
            self.chatroom_button.setText("猴子")
            return

        # 检查是否有权限打开聊天窗口
        input_text = self.keyword_input.text()
        if input_text in AppConstants.ADMIN_CODES or func_call:
            # 设置管理员权限
            is_admin = input_text == AppConstants.SUPER_ADMIN_CODE
            self.chat_window.set_admin_status(is_admin)

            # 显示聊天窗口
            self.chat_window.move(self.x() + self.width(), self.y())
            self.chat_window.show()
            self.chatroom_button.setText("关闭猴子")

            # 连接到服务器
            self.chat_window.connect_to_server()

    def show_help(self) -> None:
        """显示帮助信息"""
        self.result_area.setPlainText(AppConstants.HELP_TEXT)

    def exit_confirm(self) -> None:
        """退出确认"""
        if self.confirm_exit:
            self.chat_window.close()
            self.close()
            QApplication.quit()
            sys.exit(0)
        else:
            self.confirm_exit = True
            self.exit_button.setText("⚠️ 再次点击将退出程序")

            def reset_flag() -> None:
                time.sleep(2)
                if hasattr(self, "confirm_exit"):
                    self.confirm_exit = False
                    self.exit_button.setText("关闭")

            threading.Thread(target=reset_flag, daemon=True).start()
