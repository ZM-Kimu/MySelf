from PyQt5.QtCore import QPoint, QRect, Qt
from PyQt5.QtGui import QCursor, QMouseEvent
from PyQt5.QtWidgets import QWidget


class ResizableFramelessWindow(QWidget):
    """可调整大小的无边框窗口基类"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        # 调整大小相关属性
        self.resize_border_width = 8  # 调整区域宽度
        self.resize_mode = ""
        self.resize_start_pos = QPoint()
        self.resize_start_geometry = QRect()

        # 设置鼠标追踪
        self.setMouseTracking(True)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """鼠标按下事件"""
        if event.button() == Qt.LeftButton:
            self.resize_mode = self._get_resize_mode(event.pos())
            if self.resize_mode:
                self.resize_start_pos = event.globalPos()
                self.resize_start_geometry = self.geometry()
                event.accept()
                return
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """鼠标移动事件"""
        if event.buttons() == Qt.LeftButton and self.resize_mode:
            self._handle_resize(event.globalPos())
            event.accept()
            return

        # 更新鼠标光标
        resize_mode = self._get_resize_mode(event.pos())
        self._update_cursor(resize_mode)

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """鼠标释放事件"""
        if event.button() == Qt.LeftButton:
            self.resize_mode = ""
            self.setCursor(QCursor(Qt.ArrowCursor))
            event.accept()
            return
        super().mouseReleaseEvent(event)

    def _get_resize_mode(self, pos: QPoint) -> str:
        """获取调整模式"""
        rect = self.rect()
        border = self.resize_border_width

        # 检查是否在边缘区域
        left = pos.x() <= border
        right = pos.x() >= rect.width() - border
        top = pos.y() <= border
        bottom = pos.y() >= rect.height() - border

        if left and top:
            return "top-left"
        if right and top:
            return "top-right"
        if left and bottom:
            return "bottom-left"
        if right and bottom:
            return "bottom-right"
        if left:
            return "left"
        if right:
            return "right"
        if top:
            return "top"
        if bottom:
            return "bottom"

        return ""

    def _update_cursor(self, resize_mode: str):
        """更新鼠标光标"""
        if resize_mode in ["top-left", "bottom-right"]:
            self.setCursor(QCursor(Qt.SizeFDiagCursor))
        elif resize_mode in ["top-right", "bottom-left"]:
            self.setCursor(QCursor(Qt.SizeBDiagCursor))
        elif resize_mode in ["left", "right"]:
            self.setCursor(QCursor(Qt.SizeHorCursor))
        elif resize_mode in ["top", "bottom"]:
            self.setCursor(QCursor(Qt.SizeVerCursor))
        else:
            self.setCursor(QCursor(Qt.ArrowCursor))

    def _handle_resize(self, global_pos: QPoint):
        """处理窗口调整大小"""
        delta = global_pos - self.resize_start_pos
        new_geometry = QRect(self.resize_start_geometry)

        # 获取最小尺寸
        min_size = self.minimumSize()
        min_width = min_size.width()
        min_height = min_size.height()

        if "left" in self.resize_mode:
            new_width = max(min_width, new_geometry.width() - delta.x())
            new_geometry.setLeft(new_geometry.right() - new_width)
        elif "right" in self.resize_mode:
            new_width = max(min_width, new_geometry.width() + delta.x())
            new_geometry.setWidth(new_width)

        if "top" in self.resize_mode:
            new_height = max(min_height, new_geometry.height() - delta.y())
            new_geometry.setTop(new_geometry.bottom() - new_height)
        elif "bottom" in self.resize_mode:
            new_height = max(min_height, new_geometry.height() + delta.y())
            new_geometry.setHeight(new_height)

        self.setGeometry(new_geometry)
