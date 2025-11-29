import sys

from PyQt5.QtWidgets import QApplication

from src.main_window import MainWindow
from src.utils import RuntimeTool

if __name__ == "__main__":
    runtime_tool = RuntimeTool()
    if runtime_tool.is_program_instance_running():
        sys.exit(0)
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
