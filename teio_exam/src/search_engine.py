import re
from typing import Optional

from pynput import mouse
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QColor, QTextCharFormat, QTextCursor
from PyQt5.QtWidgets import QTextEdit


class SearchEngine(QObject):
    search_status_updated = pyqtSignal(int, int)
    find_next_match_requested = pyqtSignal()
    find_previous_match_requested = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self.current_matches: list[tuple[int, int]] = []
        self.current_match_index: int = -1
        self.current_textarea: Optional[QTextEdit] = None
        self.current_keyword: str = ""
        self.mouse_listener: Optional[mouse.Listener] = None
        self.is_mouse_pressed: bool = False

        self.find_next_match_requested.connect(self.find_next)
        self.find_previous_match_requested.connect(self.find_previous)

    @staticmethod
    def clean_text(string: str) -> str:
        """清理文本，移除特殊字符和数字"""
        return re.sub(r"[\W\d_]+", "", string, flags=re.UNICODE)

    @staticmethod
    def search_in_document(
        text: str, keyword: str, use_regex: bool = False
    ) -> list[tuple[int, str]]:
        """在文档中搜索关键字，返回匹配行的行号和内容"""
        lines = text.split("\n")
        matches: list[tuple[int, str]] = []

        if use_regex:
            try:
                pattern = re.compile(keyword, re.IGNORECASE)
                for i, line in enumerate(lines):
                    if pattern.search(line):
                        matches.append((i, line))
            except re.error:
                use_regex = False

        if not use_regex:
            keyword_clean = SearchEngine.clean_text(keyword)
            for i, line in enumerate(lines):
                if keyword_clean.lower() in SearchEngine.clean_text(line).lower():
                    matches.append((i, line))

        return matches

    def highlight_text_with_position_mapping(
        self,
        textarea: QTextEdit,
        search_text: str,
        display_positions: list[tuple[int, int]],
        keyword: str,
    ) -> int:
        """
        使用预计算的显示位置进行高亮
        """
        # 清除之前的搜索状态
        self._clear_highlights_completely(textarea)

        # 重置状态
        self.current_textarea = textarea
        self.current_keyword = keyword
        self.current_matches = display_positions
        self.current_match_index = -1

        # 设置鼠标监听器
        if not self.mouse_listener:
            self._setup_mouse_listener()

        if self.current_matches:
            # 高亮所有匹配项
            self._highlight_all_matches(textarea)
            # 设置当前匹配项为第一个
            self.current_match_index = 0
            self._highlight_current_match(textarea)
            self._jump_to_current_match(textarea)

        # 发送状态更新信号
        total_matches = len(self.current_matches)
        current_index = (
            self.current_match_index + 1 if self.current_match_index >= 0 else 0
        )
        self.search_status_updated.emit(current_index, total_matches)

        return total_matches

    def highlight_text_in_textarea(
        self, textarea: QTextEdit, text: str, keyword: str, use_regex: bool = False
    ) -> int:
        """在文本区域中高亮显示关键字并跳转到第一个匹配位置，返回匹配数量"""
        self._clear_highlights_completely(textarea)

        self.current_textarea = textarea
        self.current_keyword = keyword
        self.current_matches = []
        self.current_match_index = -1

        self._setup_mouse_listener()

        self._find_all_matches_in_text(text, keyword, use_regex)

        if self.current_matches:
            self._highlight_all_matches(textarea)
            self.current_match_index = 0
            self._highlight_current_match(textarea)
            self._jump_to_current_match(textarea)

        total_matches = len(self.current_matches)
        current_index = (
            self.current_match_index + 1 if self.current_match_index >= 0 else 0
        )
        self.search_status_updated.emit(current_index, total_matches)

        return total_matches

    def _find_all_matches_in_text(
        self, text: str, keyword: str, use_regex: bool
    ) -> None:
        """在指定文本中查找所有匹配项的位置"""
        if use_regex:
            try:
                pattern = re.compile(keyword, re.IGNORECASE)
                for match in pattern.finditer(text):
                    self.current_matches.append((match.start(), match.end()))
            except re.error:
                # 正则表达式错误时使用普通搜索
                self._find_normal_matches(text, keyword)
        else:
            self._find_normal_matches(text, keyword)

    def _clear_highlights_completely(self, textarea: QTextEdit) -> None:
        """完全清除文本区域的所有高亮"""
        if not textarea:
            return

        cursor = textarea.textCursor()
        # 保存当前光标位置
        current_position = cursor.position()

        # 选择整个文档
        cursor.select(QTextCursor.Document)

        # 创建完全清空的格式
        format_clear = QTextCharFormat()
        format_clear.setBackground(QColor())  # 显式设置为无背景色
        format_clear.clearBackground()  # 清除背景

        # 应用清空格式
        cursor.setCharFormat(format_clear)
        cursor.clearSelection()

        # 恢复光标位置
        cursor.setPosition(current_position)
        textarea.setTextCursor(cursor)

    def _find_normal_matches(self, text: str, keyword: str) -> None:
        """普通文本搜索"""
        keyword_lower = keyword.lower()
        text_lower = text.lower()
        start = 0

        while True:
            pos = text_lower.find(keyword_lower, start)
            if pos == -1:
                break
            self.current_matches.append((pos, pos + len(keyword)))
            start = pos + 1

    def _highlight_all_matches(self, textarea: QTextEdit) -> None:
        """高亮所有匹配项（黄色背景）"""
        cursor = textarea.textCursor()
        text_length = len(textarea.toPlainText())

        for start_pos, end_pos in self.current_matches:
            if start_pos >= text_length or end_pos > text_length:
                continue  # 跳过越界的位置

            cursor.setPosition(start_pos)
            cursor.setPosition(end_pos, QTextCursor.KeepAnchor)

            format_highlight = QTextCharFormat()
            format_highlight.setBackground(QColor(255, 255, 0))
            cursor.mergeCharFormat(format_highlight)
            cursor.clearSelection()

    def _highlight_current_match(self, textarea: QTextEdit):
        """高亮当前选中的匹配项（棕色背景）"""
        if self.current_match_index < 0 or self.current_match_index >= len(
            self.current_matches
        ):
            return

        cursor = textarea.textCursor()
        start_pos, end_pos = self.current_matches[self.current_match_index]
        text_length = len(textarea.toPlainText())

        if start_pos >= text_length or end_pos > text_length:
            return

        cursor.setPosition(start_pos)
        cursor.setPosition(end_pos, QTextCursor.KeepAnchor)

        format_current = QTextCharFormat()
        format_current.setBackground(QColor(165, 42, 42))  # 棕色背景
        cursor.mergeCharFormat(format_current)
        cursor.clearSelection()

    def _jump_to_current_match(self, textarea: QTextEdit):
        """跳转到当前匹配项"""
        if self.current_match_index < 0 or self.current_match_index >= len(
            self.current_matches
        ):
            return

        cursor = textarea.textCursor()
        start_pos, _ = self.current_matches[self.current_match_index]

        text_length = len(textarea.toPlainText())
        if start_pos >= text_length:
            return

        cursor.setPosition(start_pos)
        textarea.setTextCursor(cursor)
        textarea.ensureCursorVisible()

    def find_next(self) -> bool:
        """查找下一个匹配项"""
        if not self.current_matches or not self.current_textarea:
            return False

        # 清除当前高亮
        self._highlight_all_matches(self.current_textarea)

        # 移动到下一个
        self.current_match_index = (self.current_match_index + 1) % len(
            self.current_matches
        )

        # 高亮新的当前项
        self._highlight_current_match(self.current_textarea)
        self._jump_to_current_match(self.current_textarea)

        # 更新状态
        self.search_status_updated.emit(
            self.current_match_index + 1, len(self.current_matches)
        )
        return True

    def find_previous(self) -> bool:
        """查找上一个匹配项"""
        if not self.current_matches or not self.current_textarea:
            return False

        # 清除当前高亮
        self._highlight_all_matches(self.current_textarea)

        # 移动到上一个
        self.current_match_index = (self.current_match_index - 1) % len(
            self.current_matches
        )

        # 高亮新的当前项
        self._highlight_current_match(self.current_textarea)
        self._jump_to_current_match(self.current_textarea)

        # 更新状态
        self.search_status_updated.emit(
            self.current_match_index + 1, len(self.current_matches)
        )
        return True

    def _setup_mouse_listener(self):
        """设置鼠标监听器"""
        if self.mouse_listener:
            self.mouse_listener.stop()

        def on_click(_x, _y, button, pressed):
            if button == mouse.Button.left:
                self.is_mouse_pressed = pressed

        def on_scroll(_x, _y, _dx, dy):
            if self.is_mouse_pressed and self.current_textarea:
                if dy > 0:  # 向上滚动
                    self.find_previous_match_requested.emit()
                else:  # 向下滚动
                    self.find_next_match_requested.emit()

        self.mouse_listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
        self.mouse_listener.start()

    def clear_search(self) -> None:
        """清除搜索状态"""
        if self.current_textarea:
            self._clear_highlights_completely(self.current_textarea)
            # cursor = self.current_textarea.textCursor()
            # cursor.select(QTextCursor.Document)
            # format_clear = QTextCharFormat()
            # cursor.mergeCharFormat(format_clear)
            # cursor.clearSelection()

        self.current_matches = []
        self.current_match_index = -1
        self.current_textarea = None
        self.current_keyword = ""

        if self.mouse_listener:
            self.mouse_listener.stop()
            self.mouse_listener = None

    def get_search_status(self) -> tuple[int, int]:
        """获取搜索状态 (当前索引, 总数)"""
        current_index = (
            self.current_match_index + 1 if self.current_match_index >= 0 else 0
        )
        total_matches = len(self.current_matches)
        return current_index, total_matches
