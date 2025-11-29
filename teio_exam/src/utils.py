import socket


class RuntimeTool:
    SOCKET_PORT = 26984

    def __init__(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def is_program_instance_running(self) -> bool:
        try:
            self.socket.bind(("127.0.0.1", RuntimeTool.SOCKET_PORT))
            self.socket.listen(1)
            return False
        except:
            return True


class AppConstants:
    APP_TITLE = "帝王题目检索器 专业版v2.0"
    ADMIN_CODES = ["1145141919810", "233332"]
    SUPER_ADMIN_CODE = "1145141919810"

    WELCOME_TEXT = """结果于此显示
🌟🌟🌟🌟🌟🌟🌟
💡 帝王题目检索器 史诗版v2.0 💡
🙏老天保佑✨金山💰银山🏔️前路有🚀
🌟🌟🌟🌟🌟🌟🌟"""

    HELP_TEXT = """按下鼠标中键：置顶或取消置顶窗口
按下鼠标右键：移动窗口到鼠标
使用鼠标滚轮与左右键执行动作：
上上下下左左右右：显示或隐藏主界面
上下上下：启用极简模式，只需Ctrl+C复制文本即可查询
猴子：在输入框中输入代号以使用
[关键字]: 通过一段文本检索指定题目"""
