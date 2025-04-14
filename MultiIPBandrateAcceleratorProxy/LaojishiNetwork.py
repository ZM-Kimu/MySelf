import os
import subprocess
import sys
import threading
import tkinter as tk
from time import sleep
from tkinter import PhotoImage, ttk

import pystray
from PIL import Image
from pystray import MenuItem as item

from networkDelivery import (
    delete_ip_address,
    disable_http_proxy,
    disable_socks_proxy,
    get_available_ip,
    set_http_proxy,
    set_ip_address,
    set_socks_proxy,
)


class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("老技师网络攻占器")
        self.root.geometry("350x280")
        self.root.iconphoto(
            False,
            PhotoImage(
                file=(
                    os.path.join(sys._MEIPASS, "icon.png")
                    if getattr(sys, "frozen", False)
                    else "icon.png"
                )
            ),
        )

        # 标题
        self.title_label = tk.Label(
            root,
            text="老技师网络攻占器☆超级增强版☆",
            font=("黑体", 13, "bold"),
        )
        self.title_label.pack(pady=5)

        # 提示文字
        self.notice_label = tk.Label(
            root, text="网速增强工具 v0.1 (需要多线程下载器)", font=("黑体", 10)
        )
        self.notice_label.pack(pady=5)

        # 输入框和下拉菜单框架
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        # 端口标签
        self.port_label = tk.Label(self.input_frame, text="端口")
        self.port_label.grid(row=0, column=0, padx=10, pady=(0, 5), sticky="s")

        # 端口输入框
        self.port_entry = tk.Entry(self.input_frame, width=10)
        self.port_entry.grid(row=1, column=0, padx=10)
        self.port_entry.insert(0, "40900")

        # 协议标签
        self.protocol_label = tk.Label(self.input_frame, text="协议")
        self.protocol_label.grid(row=0, column=1, padx=10, pady=(0, 5), sticky="s")

        # 协议下拉菜单
        self.combobox = ttk.Combobox(self.input_frame, values=["socks"], width=10)
        self.combobox.grid(row=1, column=1, padx=10)
        self.combobox.set("socks")

        # 攻占IP标签
        self.ip_label = tk.Label(self.input_frame, text="攻占数量")
        self.ip_label.grid(row=0, column=2, padx=10, pady=(0, 5), sticky="s")

        # 攻占IP输入框
        self.ip_entry = tk.Entry(self.input_frame, width=5)
        self.ip_entry.grid(row=1, column=2, padx=10)
        self.ip_entry.insert(0, "15")

        # 代理设置复选框
        self.proxy_var = tk.BooleanVar()
        self.proxy_check = tk.Checkbutton(
            root, text="自动设置成系统代理", variable=self.proxy_var
        )
        self.proxy_check.pack(pady=5)

        # 启动按钮
        self.start_button = tk.Button(
            root, text="启动！", font=("黑体", 16, "bold"), command=self.start
        )
        self.start_button.pack(pady=15)

        # 状态提醒
        self.status_label = tk.Label(root, text="未攻占", font=("黑体", 10))
        self.status_label.pack(pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.toggle_window)
        # 创建托盘图标
        self.icon_image = Image.open(
            os.path.join(sys._MEIPASS, "icon.ico")
            if getattr(sys, "frozen", False)
            else "icon.ico"
        )  # 请确保有一个名为icon.png的图标文件
        self.icon = pystray.Icon(
            "ljs", self.icon_image, "老技师网络攻占器", self.create_menu()
        )
        self.tray_thread = None
        self.show_icon()
        self.stop = False
        self.ips = []
        self.adapter = ""
        self.port = 0
        self.protocol = ""
        self.ip_num = 0
        self.is_proxy = False
        self.process = None
        self.monitor_thread = None

    def start(self):
        try:
            self.stop = True
            delete_ip_address(self.adapter, self.ips)
            self.protocol = self.combobox.get()
            self.port = int(self.port_entry.get())
            self.ip_num = int(self.ip_entry.get())
            self.is_proxy = self.proxy_var.get()
            self.write("开始攻占 正在取得可用ip地址...")
            # 这里可以添加启动逻辑
            self.ips, self.adapter = get_available_ip()
            self.write(f"{len(self.ips)}个地址可被攻占")
            self.ips = self.ips[: min(self.ip_num, len(self.ips))]
            set_ip_address(self.adapter, self.ips)
            command = [
                (
                    os.path.join(sys._MEIPASS, "dispatch.exe")
                    if getattr(sys, "frozen", False)
                    else "dispatch.exe"
                ),
                "start",
                "--host",
                "127.0.0.1",
                "--port",
                str(self.port),
            ]
            if self.protocol == "http":
                command.append("--http")
            self.monitor_thread = threading.Thread(
                target=self.monitor_process,
                args=(command,),
            )
            if self.is_proxy:
                if self.protocol == "socks":
                    set_socks_proxy(self.port)
                else:
                    set_http_proxy(self.port)
            self.stop = False
            self.monitor_thread.start()
            self.write(f"代理服务器位于：{self.protocol}://127.0.0.1:{self.port}")
        except Exception as err:
            self.write(f"攻占失败\n{str(err)}")

    def create_menu(self):
        return (
            item("显示/隐藏主界面", self.toggle_window),
            item("关闭", self.exit_app),
        )

    def toggle_window(self):
        if self.root.state() == "withdrawn":
            self.root.deiconify()
        else:
            self.root.withdraw()
            self.show_icon()

    def show_icon(self):
        if not self.tray_thread or not self.tray_thread.is_alive():
            self.tray_thread = threading.Thread(target=self.icon.run)
            self.tray_thread.start()

    def exit_app(self, icon, item):
        self.stop = True
        self.write("清除地址中...")
        delete_ip_address(self.adapter, self.ips)
        if self.is_proxy:
            if self.protocol == "socks":
                disable_socks_proxy()
            else:
                disable_http_proxy()
        if self.icon:
            self.icon.stop()
        self.root.quit()
        os._exit(0)

    def write(self, text):
        self.status_label.config(text=text)
        self.root.update()

    def monitor_process(self, command):
        while not self.stop:
            if self.process is None or self.process.poll() is not None:
                self.process = subprocess.Popen(
                    command#, creationflags=subprocess.CREATE_NO_WINDOW
                )
            sleep(4)
        if self.process:
            self.process.terminate()


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
