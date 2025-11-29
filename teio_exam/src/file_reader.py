import os
import sys


class FileReader:
    @staticmethod
    def resource_path(relative_path: str) -> str:
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(getattr(sys, "_MEIPASS"), relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
