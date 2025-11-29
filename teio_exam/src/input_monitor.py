from collections.abc import Callable
from typing import TYPE_CHECKING, Optional

from pynput import mouse
from PyQt5.QtCore import QObject, QTimer, pyqtSignal
from PyQt5.QtWidgets import QApplication

if TYPE_CHECKING:
    from src.main_window import MainWindow


class ClipboardMonitor:
    def __init__(
        self, app: "MainWindow", on_text_change: Optional[Callable] = None
    ) -> None:
        self.app = app
        self.clipboard = QApplication.clipboard()
        self.last_text = self.clipboard.text().strip()
        self.first_change = True
        self.on_text_change = on_text_change or self.default_handler

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_clipboard)
        self.timer.start(300)

    def check_clipboard(self) -> None:
        current = self.clipboard.text().strip()
        if current and current != self.last_text:
            if self.first_change:
                self.first_change = False
                return
            self.last_text = current
            self.on_text_change(current)

    def default_handler(self, text: str) -> None:
        print("📋 新复制内容：", text)


class MouseSequenceListener(QObject):
    uuddllrr_match_signal = pyqtSignal()
    udud_match_signal = pyqtSignal()
    udlr_match_signal = pyqtSignal()
    click_event_signal = pyqtSignal(mouse.Button)
    scroll_event_signal = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.sequence: list[str] = []
        self.uuddllrr_target = ["wu", "wu", "wd", "wd", "l", "l", "r", "r"]
        self.udud_target = ["wu", "wd", "wu", "wd", "wu", "wd", "wu", "wd"]
        self.udlr_target = ["wu", "wd", "l"]
        self.listener = mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll)
        self.listener.start()

        self.last_scroll_dir = ""
        self.event_timer = QTimer()
        self.event_timer.setSingleShot(True)
        self.event_timer.timeout.connect(self.clear_scroll)
        self.scroll_event_signal.connect(self._handle_scroll_event)
        self.click_event_signal.connect(self._handle_click_event)

    def on_click(self, _x, _y, button, pressed) -> None:
        if not pressed:
            return
        self.click_event_signal.emit(button)

    def _handle_click_event(self, button: mouse.Button) -> None:
        if button == mouse.Button.left:
            self._append("l")
        elif button == mouse.Button.right:
            self._append("r")
        self.event_timer.start(150)

    def on_scroll(self, _x, _y, _dx, dy) -> None:
        direction = "wu" if dy > 0 else "wd"
        self.scroll_event_signal.emit(direction)

    def _handle_scroll_event(self, direction: str) -> None:
        if direction != self.last_scroll_dir or not self.event_timer.isActive():
            self._append(direction)

        self.last_scroll_dir = direction
        self.event_timer.start(150)

    def _append(self, code) -> None:
        self.sequence.append(code)
        if len(self.sequence) > len(self.uuddllrr_target):
            self.sequence.pop(0)
        if self.sequence[-len(self.uuddllrr_target) :] == self.uuddllrr_target:
            self.uuddllrr_match_signal.emit()
            self.sequence.clear()
        if self.sequence[-len(self.udud_target) :] == self.udud_target:
            self.udud_match_signal.emit()
            self.sequence.clear()
        if self.sequence[-len(self.udlr_target) :] == self.udlr_target:
            self.udlr_match_signal.emit()
            self.sequence.clear()

    def clear_scroll(self) -> None:
        self.last_scroll_dir = ""
