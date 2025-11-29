import base64
import re

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap, QTextCursor, QTextDocument, QTextImageFormat
from PyQt5.QtWidgets import QTextEdit


class ImageProcessor:
    """处理文本中的base64图片"""

    IMAGE_PATTERN = re.compile(r"<!image!>(.*?)<¡ǝƃɐɯı¡>", re.DOTALL)

    def __init__(self):
        self.position_mapping = {}  # 原始位置 -> 显示位置的映射

    @staticmethod
    def extract_images_from_text(text: str) -> list[tuple[str, str, int, int]]:
        """从文本中提取所有图片信息"""
        images = []
        for match in ImageProcessor.IMAGE_PATTERN.finditer(text):
            full_match = match.group(0)
            base64_data = match.group(1).strip()
            start_pos = match.start()
            end_pos = match.end()
            images.append((full_match, base64_data, start_pos, end_pos))
        return images

    @staticmethod
    def get_text_only_for_search(text: str) -> str:
        """
        获取仅包含文本的版本用于搜索，完全移除图片标记
        """
        return ImageProcessor.IMAGE_PATTERN.sub("", text)

    @staticmethod
    def base64_to_pixmap(
        base64_string: str, max_width: int = 400, max_height: int = 300
    ) -> QPixmap:
        """将base64字符串转换为QPixmap"""
        try:
            if base64_string.startswith("data:image"):
                base64_string = base64_string.split(",")[1]

            image_data = base64.b64decode(base64_string)
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)

            if not pixmap.isNull():
                pixmap = pixmap.scaled(
                    max_width,
                    max_height,
                    aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
                    transformMode=Qt.TransformationMode.SmoothTransformation,
                )

            return pixmap
        except Exception as e:
            print(f"Error converting base64 to pixmap: {e}")
            return QPixmap()

    def insert_images_into_textarea(
        self, textarea: QTextEdit, original_text: str
    ) -> tuple[str, dict[int, int]]:
        """
        将文本中的base64图片标记替换为实际图片
        返回: (纯文本内容, 原始位置到显示位置的映射)
        """
        position_map = {}

        # 提取所有图片
        images = self.extract_images_from_text(original_text)

        if not images:
            textarea.setPlainText(original_text)
            return original_text, {}

        # 创建文档和光标
        document = textarea.document()
        cursor = QTextCursor(document)
        cursor.movePosition(QTextCursor.Start)
        cursor.select(QTextCursor.Document)
        cursor.removeSelectedText()

        current_pos = 0
        display_pos = 0
        text_only = ""

        for i, (full_match, base64_data, start_pos, end_pos) in enumerate(images):
            # 添加图片前的文本
            before_text = original_text[current_pos:start_pos]
            cursor.insertText(before_text)
            text_only += before_text

            # 更新位置映射
            for j in range(len(before_text)):
                position_map[current_pos + j] = display_pos + j

            display_pos += len(before_text)

            # 创建并插入图片
            pixmap = self.base64_to_pixmap(base64_data)
            if not pixmap.isNull():
                image_name = f"image_{i}_{current_pos}"
                document.addResource(
                    QTextDocument.ImageResource, QUrl(image_name), pixmap
                )

                image_format = QTextImageFormat()
                image_format.setName(image_name)
                image_format.setWidth(pixmap.width())
                image_format.setHeight(pixmap.height())

                cursor.insertImage(image_format)
                display_pos += 1  # 图片在显示中占用一个字符位置

            current_pos = end_pos

        # 添加剩余的文本
        remaining_text = original_text[current_pos:]
        cursor.insertText(remaining_text)
        text_only += remaining_text

        # 更新剩余文本的位置映射
        for j in range(len(remaining_text)):
            position_map[current_pos + j] = display_pos + j

        return text_only, position_map

    def map_search_positions_to_display(
        self, search_positions: list[tuple[int, int]], position_map: dict[int, int]
    ) -> list[tuple[int, int]]:
        """
        将搜索结果的位置映射到显示位置
        """
        display_positions = []

        for start_pos, end_pos in search_positions:
            # 查找映射后的位置
            display_start = position_map.get(start_pos)
            display_end = position_map.get(end_pos - 1)  # end_pos是排他的

            if display_start is not None and display_end is not None:
                display_positions.append((display_start, display_end + 1))

        return display_positions
