# import threading
# from typing import TYPE_CHECKING, Optional

# import mss
# import numpy as np
# from PIL import Image
# from PyQt5.QtCore import QObject, QPoint, QRect, Qt, QTimer, pyqtSignal
# from PyQt5.QtGui import QColor, QCursor, QMouseEvent, QPainter, QPen
# from PyQt5.QtWidgets import QApplication, QWidget

# from src.window_manager import TopmostWidget

# if TYPE_CHECKING:
#     from paddleocr import PaddleOCR


# class OCREngine(QObject):
#     ocr_completed = pyqtSignal(str)  # OCR完成信号
#     initialization_completed = pyqtSignal()  # 初始化完成信号

#     def __init__(self) -> None:
#         super().__init__()
#         self.ocr_engine: Optional[PaddleOCR] = None
#         self.is_initialized = False
#         self.is_initializing = False

#     def initialize_async(self) -> None:
#         """异步初始化OCR引擎"""
#         if self.is_initialized or self.is_initializing:
#             return

#         self.is_initializing = True

#         def _init() -> None:
#             try:
#                 from paddleocr import PaddleOCR

#                 self.ocr_engine = PaddleOCR(
#                     use_angle_cls=False, lang="ch", device="cpu"
#                 )
#                 self.is_initialized = True
#                 self.initialization_completed.emit()
#             except Exception as e:
#                 print(f"OCR初始化失败: {e}")
#             finally:
#                 self.is_initializing = False

#         threading.Thread(target=_init, daemon=True).start()

#     def recognize_image(self, image_array: np.ndarray) -> None:
#         """识别图像中的文字"""
#         if not self.is_initialized or not self.ocr_engine:
#             self.ocr_completed.emit("")
#             return

#         def _recognize() -> None:
#             try:
#                 if not self.ocr_engine:
#                     self.ocr_completed.emit("")
#                     return

#                 result = self.ocr_engine.predict(image_array)
#                 for res in result:
#                     texts = res.get("rec_texts", [])
#                     self.ocr_completed.emit("".join(texts))

#             except Exception as e:
#                 print(f"OCR识别失败: {e}")
#                 self.ocr_completed.emit("")

#         threading.Thread(target=_recognize, daemon=True).start()


# class ScreenCaptureWidget(QWidget):
#     capture_completed = pyqtSignal(np.ndarray)

#     def __init__(self) -> None:
#         super().__init__()
#         self.start_point: QPoint | None = None
#         self.end_point: QPoint | None = None

#         self.topmost_widget = TopmostWidget(self)

#         self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)

#         screen = QApplication.primaryScreen()
#         screen_geometry = screen.geometry()
#         self.setGeometry(screen_geometry)

#         self.topmost_widget.enable = False
#         QTimer.singleShot(400, self.topmost_widget.enforce_topmost_forever)

#     def start_capture(self) -> None:
#         """开始截图"""
#         self.start_point = None
#         self.end_point = None

#         # QApplication.setOverrideCursor(QCursor(Qt.CrossCursor))

#         self.showFullScreen()
#         self.raise_()
#         self.activateWindow()
#         self.setFocus()

#     def mousePressEvent(self, event: QMouseEvent) -> None:
#         if event.button() == Qt.LeftButton:
#             self.start_point = event.pos()

#     def mouseMoveEvent(self, event: QMouseEvent) -> None:
#         if self.start_point is not None:
#             self.end_point = event.pos()
#             self.update()

#     def mouseReleaseEvent(self, event: QMouseEvent) -> None:
#         if (
#             (event.button() == Qt.LeftButton)
#             and self.start_point is not None
#             and self.end_point is not None
#         ):
#             rect = QRect(self.start_point, self.end_point).normalized()

#             # self.releaseMouse()
#             # QApplication.restoreOverrideCursor()
#             # self._finish_capture()
#             self._capture_screen_region(rect)
#             self.hide()

#     def paintEvent(self, _event) -> None:
#         painter = QPainter(self)
#         painter.fillRect(self.rect(), QColor(0, 0, 0, 1))

#         if self.start_point is not None and self.end_point is not None:
#             rect = QRect(self.start_point, self.end_point).normalized()
#             painter.setCompositionMode(QPainter.CompositionMode_Clear)
#             painter.fillRect(rect, QColor(0, 0, 0, 0))

#             painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
#             pen = QPen(QColor(255, 0, 0), 2)
#             painter.setPen(pen)
#             painter.drawRect(rect)

#     def _capture_screen_region(self, rect: QRect) -> None:
#         """截取指定区域的屏幕内容"""
#         try:
#             with mss.mss() as sct:
#                 # 转换坐标
#                 monitor = {
#                     "top": rect.y(),
#                     "left": rect.x(),
#                     "width": rect.width(),
#                     "height": rect.height(),
#                 }

#                 # 截图
#                 screenshot = sct.grab(monitor)
#                 img_array = np.array(
#                     Image.frombytes(
#                         "RGB", screenshot.size, screenshot.bgra, "raw", "BGRX"
#                     )
#                 )

#                 self.capture_completed.emit(img_array)

#         except Exception as e:
#             print(f"截图失败: {e}")


# class OCRCaptureManager(QObject):
#     text_recognized = pyqtSignal(str)
#     capture_finished = pyqtSignal()

#     def __init__(self) -> None:
#         super().__init__()
#         self.ocr_engine = OCREngine()
#         self.capture_widget = ScreenCaptureWidget()

#         self.capture_widget.capture_completed.connect(self.ocr_engine.recognize_image)
#         self.ocr_engine.ocr_completed.connect(self.text_recognized.emit)

#         self.ocr_engine.initialize_async()

#     def _on_ocr_completed(self, text: str) -> None:
#         """OCR完成后的处理"""
#         self.text_recognized.emit(text)
#         self.capture_finished.emit()

#     def start_capture(self) -> None:
#         """开始截图OCR流程"""
#         if self.ocr_engine.is_initialized:
#             self.capture_widget.start_capture()

#     def is_ocr_ready(self) -> bool:
#         """检查OCR是否准备就绪"""
#         return self.ocr_engine.is_initialized
