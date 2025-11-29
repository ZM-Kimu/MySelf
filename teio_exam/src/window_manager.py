import threading
import time
from typing import TYPE_CHECKING

import win32con
import win32gui
from pynput import mouse
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QWidget

if TYPE_CHECKING:
    from src.main_window import MainWindow


class TopmostWidget:
    def __init__(self, window: "MainWindow | QWidget") -> None:
        self.enable = True
        self.window = window

    def get_hwnd(self) -> int:
        self.window.show()  # 确保窗口已创建
        qt_win = QWindow.fromWinId(self.window.winId())
        hwnd = int(qt_win.winId())
        return hwnd

    def force_topmost(self) -> None:
        hwnd = self.get_hwnd()
        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_TOPMOST,
            0,
            0,
            0,
            0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE,
        )
        try:
            win32gui.BringWindowToTop(hwnd)
            win32gui.SetForegroundWindow(hwnd)
        except Exception as e:
            print(f"[警告] BringWindowToTop/SetForegroundWindow 失败：{e}")

    def enforce_topmost_forever(self) -> None:
        def loop() -> None:
            while True:
                if self.enable and not self._is_focused_on_chat():
                    self.force_topmost()
                time.sleep(0.5)

        threading.Thread(target=loop, daemon=True).start()

    def toggle_topmost(self) -> None:
        self.enable = not self.enable
        win32gui.SetWindowPos(
            self.get_hwnd(),
            win32con.HWND_TOPMOST if self.enable else win32con.HWND_NOTOPMOST,
            0,
            0,
            0,
            0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE,
        )

    def _is_focused_on_chat(self) -> bool:
        if (
            hasattr(self.window, "chat_window")
            and self.window.chat_window.isActiveWindow()
        ):
            return True
        return False


class EventBridge(QObject):
    right_click_move_signal = pyqtSignal(QWidget, int, int)
    middle_click_topmost_signal = pyqtSignal(QWidget)
    toggle_show_hidd_signal = pyqtSignal()
    toggle_pure_mode = pyqtSignal()


class MouseEventHandler:
    @staticmethod
    def move_window_position(window: "MainWindow", x: int, y: int) -> None:
        window.move(x - window.width() // 2, y - window.height() // 2)

    @staticmethod
    def toggle_topmost(window: "MainWindow") -> None:
        window.topmost_widget.toggle_topmost()

    @staticmethod
    def setup_global_mouse_listener(
        event_bridge: EventBridge, window: "MainWindow"
    ) -> None:
        def on_click(x, y, button, pressed) -> None:
            try:
                if pressed and window.isVisible():
                    if button == mouse.Button.right:
                        event_bridge.right_click_move_signal.emit(window, x, y)
                    elif button == mouse.Button.middle:
                        event_bridge.middle_click_topmost_signal.emit(window)
            except:
                pass

        mouse.Listener(on_click=on_click).start()
