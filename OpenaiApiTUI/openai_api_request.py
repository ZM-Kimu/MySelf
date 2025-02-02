"""
This script is designed to mimic the OpenAI API interface with CogVLM2 Chat
It demonstrates how to integrate image and text-based input to generate a response.
Currently, the model can only handle a single image.
Therefore, do not use this script to process multiple images in one conversation. (includes images from history)
And it only works on the chat model, not the base model.
"""

import base64
import json
import msvcrt
import os
import sys
import time
from typing import Any, Dict, List, Literal

import requests

base_url = "http://0.0.0.0:8000"
messages = []


def create_chat_completion(
    model, message, temperature=0.8, max_tokens=2048, top_p=0.8, use_stream=False
):
    """
    This function sends a request to the chat API to generate a response based on the given messages.
    Args:
        model (str): The name of the model to use for generating the response.
        messages (list): A list of message dictionaries representing the conversation history.
        temperature (float): Controls randomness in response generation. Higher values lead to more random responses.
        max_tokens (int): The maximum length of the generated response.
        top_p (float): Controls diversity of response by filtering less likely options.
        use_stream (bool): Determines whether to use a streaming response or a single response.

    The function constructs a JSON payload with the specified parameters and sends a POST request to the API.
    It then handles the response, either as a stream (for ongoing responses) or a single message.
    """
    global messages
    data = {
        "model": model,
        "messages": message,
        "stream": use_stream,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
    }

    response = requests.post(
        f"{base_url}/v1/chat/completions", json=data, stream=use_stream
    )
    if response.status_code == 200:
        if use_stream:
            # 处理流式响应
            content = ""
            for line in response.iter_lines():
                time.sleep(stream_slow_time)
                if line:
                    decoded_line = line.decode("utf-8")[6:]
                    try:
                        response_json = json.loads(decoded_line)
                        part = (
                            response_json.get("choices", [{}])[0]
                            .get("delta", {})
                            .get("content", "")
                        )
                        content += part
                        print(part)
                    except:
                        print("Special Token:", decoded_line)
            json_content = {
                "role": "assistant",
                "content": content.rstrip("--!"),
            }

        else:
            # 处理非流式响应
            decoded_line = response.json()
            json_content = decoded_line.get("choices", [{}])[0].get("message", "")
            json_content["content"] = json_content["content"].rstrip("--!")
            content = json_content.get("content", "")
            print(content)
        if json_content.get("content", "").rstrip("--!"):
            messages = message.copy()
            messages.append(json_content)
    else:
        print("Error:", response.status_code)
        return None


def encode_image(image_path):
    """
    Encodes an image file into a base64 string.
    Args:
        image_path (str): The path to the image file.

    This function opens the specified image file, reads its content, and encodes it into a base64 string.
    The base64 encoding is used to send images over HTTP as text.
    """

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def simple_image_chat(use_stream=True, temperature=0.8, max_tokens=2048, top_p=0.8):
    """
    Facilitates a simple chat interaction involving an image.

    Args:
        use_stream (bool): Specifies whether to use streaming for chat responses.
        img_path (str): Path to the image file to be included in the chat.

    This function encodes the specified image and constructs a predefined conversation involving the image.
    It then calls `create_chat_completion` to generate a response from the model.
    The conversation includes asking about the content of the image and a follow-up question.
    """
    img_path = input("ImagePath:")
    message = prefix + input("Message:")

    messaging = {"role": "user", "content": [{"type": "text", "text": message}]}
    if img_path:
        img_url = f"data:image/jpeg;base64,{encode_image(img_path.strip())}"
        messaging["content"].append(
            {"type": "image_url", "image_url": {"url": img_url}}
        )
    if not (img_path or messages):
        img_url = "data:image/jpeg;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAANSURBVBhXY2BgYPgPAAEEAQBwIGULAAAAAElFTkSuQmCC"
        messaging["content"].append(
            {"type": "image_url", "image_url": {"url": img_url}}
        )
    temp_message = messages.copy()
    temp_message.append(messaging)

    create_chat_completion(
        "cogvlm2",
        message=temp_message,
        use_stream=use_stream,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
    )


temperature = 0.8
max_tokens = 2048
top_p = 0.8
stream = False
log = False
prefix = ""
port = 8000
stream_slow_time = 0


def console_advanced_options():
    global temperature, max_tokens, top_p, stream, log
    if "n" not in input("启用高级选项？[y]/n"):
        temperature = input("Temperature[0.8]0-1: ")
        temperature = float(temperature) if temperature else 0.8
        max_tokens = input("Max_tokens[2048]: ")
        max_tokens = int(max_tokens) if max_tokens else 2048
        top_p = input("Top_p[0.8]0-1: ")
        top_p = float(top_p) if top_p else 0.8
        stream = "y" in input("启用流式传输？ y/[n]")
        log = "y" in input("启用日志？ y/[n]")
    else:
        temperature = 0.8
        max_tokens = 2048
        top_p = 0.8


def clean_conversation():
    global messages
    messages = []


def create_inherence_prompt():
    global prefix
    print(f"现在的固有提示词是：{prefix}")
    prefix = input("更改提示词：")


def interrupt_exist_chat():
    requests.get(f"{base_url}/v1/interrupt")


def get_op() -> None | Literal["ENTER"] | Literal["LEFT"] | Literal["RIGHT"]:
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b"\r":
                return "ENTER"
            if key == b"\xe0":  # Special key prefix
                key = msvcrt.getch()
                if key == b"K":
                    return "LEFT"
                if key == b"M":
                    return "RIGHT"


def debug():
    global stream_slow_time
    print(f"流式传输每数据间的接收时间：{stream_slow_time}")
    stream_slow_time = float(input("更改流式传输时间："))


def change_port():
    global port
    port = 8000
    sys.stdout.write("Port in: \033[100m\033[37m8000\033[0m/8001")
    while True:
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        op = get_op()
        if op == "RIGHT":
            sys.stdout.write("Port in: 8000/\033[100m\033[37m8001\033[0m")
            port = 8001
        if op == "LEFT":
            sys.stdout.write("Port in: \033[100m\033[37m8000\033[0m/8001")
            port = 8000
        if op == "ENTER":
            print()
            return port
        sys.stdout.flush()


def change_conversation():
    cursor_x = cursor_y = page_start = editor_start = 0
    is_edit = False
    editable_message = []
    for message in messages:
        if message["role"] == "user":
            editable_message.append(
                {"text": "你：", "selectable": False, "type": "text"}
            )
            for content in message["content"]:
                if content["type"] == "text":
                    editable_message.append(
                        {
                            "text": f"{content['text']}",
                            "selectable": True,
                            "type": "text",
                        }
                    )
                if content["type"] == "image_url":
                    editable_message.append(
                        {"text": "你：", "selectable": False, "type": "text"}
                    )
                    editable_message.append(
                        {
                            "text": f"{content['image_url']['url']}",
                            "selectable": True,
                            "type": "image",
                        }
                    )
        if message["role"] == "assistant":
            editable_message.append(
                {"text": "VLM：", "selectable": False, "type": "text"}
            )
            editable_message.append(
                {"text": f"{message['content']}", "selectable": True, "type": "text"}
            )
    while True:
        os.system("cls")
        terminal_size = os.get_terminal_size()
        if not messages:
            sys.stdout.write(
                f"\033[47m\033[30m\033[1m{(terminal_size.columns - 10) // 2 * ' '}记录不存在{(terminal_size.columns - 10) // 2 * ' '}\033[0m"
            )
            sys.stdout.write(f"\033[{cursor_y - page_start + 1};{cursor_x + 1}H")
            status = "\033[47m\033[30m\033[1mChatVLM会话编辑器 任意键退出\033[0m"
            sys.stdout.write(f"\033[{terminal_size.lines};1H")
            sys.stdout.write(status.ljust(terminal_size.columns - 1))
            sys.stdout.flush()
            msvcrt.getch()
            print()
            break
        text_size_y = min(terminal_size.lines // 1.3 - 1, len(editable_message))
        editor_start = page_start * text_size_y + editor_start % text_size_y
        text_start_offset = max(cursor_y - (terminal_size.lines // 1.3 - 2), 0)
        if editor_start == 0:
            editor_end = text_size_y
        if cursor_y > text_size_y + editor_start - 1 or cursor_y < editor_start:
            editor_start = page_start + text_start_offset
            editor_end = editor_start + text_size_y
        if editor_start % text_size_y == 0 and editor_start != 0:
            page_start += 1
        if not editable_message[cursor_y]["selectable"]:
            for index, row in enumerate(editable_message):
                if index > cursor_y and row["selectable"]:
                    cursor_y = min(len(editable_message) - 1, index)
                    break
        for line in range(editor_start, editor_end):
            editable_line = editable_message[line]
            if editable_line["type"] == "image":
                if editable_line.get("changing", False):
                    text = "(键入路径以更改图片)\n"
                    if editable_line:
                        text = editable_line["text"]
                else:
                    text = f"...{editable_line['text'][-10:]}(发送图片)"
            else:
                text = (
                    editable_line["text"][: len(editable_line["text"]) // 3]
                    if len(editable_line["text"]) > terminal_size.columns // 2
                    else editable_line["text"]
                )
            if line == cursor_y:
                if is_edit:
                    for index, word in enumerate(text):
                        if index == cursor_x:
                            sys.stdout.write(f"\033[100m\033[37m{word}\033[0m")
                            continue
                        sys.stdout.write(f"\033[30m\033[47m{word}\033[0m")
                    if cursor_x > len(text) - 1:
                        sys.stdout.write("\033[100m\033[30m \033[0m")
                else:
                    sys.stdout.write(f"\033[47m\033[30m{text}\033[0m")
                print()
            else:
                print(text)
        sys.stdout.write(f"\033[{cursor_y - page_start + 1};{cursor_x + 1}H")
        status = f"\033[47m\033[30m\033[1mChatVLM会话编辑器 模式: {'编辑' if is_edit else '选择'} | {'ESC以退出编辑模式' if is_edit else '回车以编辑, ESC以退出'}\033[0m"
        sys.stdout.write(f"\033[{terminal_size.lines};1H")
        sys.stdout.write(status.ljust(terminal_size.columns - 1))
        sys.stdout.flush()
        key = msvcrt.getwch()
        if key == "\r":  # Enter
            if not is_edit:
                is_edit = True
                if editable_message[cursor_y]["type"] == "image":
                    editable_message[cursor_y]["changing"] = True
                    editable_message[cursor_y]["text"] = ""
        elif (
            not key in ("\xe0", "\x1b")
            and editable_message[cursor_y]["type"] == "image"
            and editable_message[cursor_y].get("changing", False)
        ):  # Receive image path
            if editable_message[cursor_y].get(
                "changing", False
            ):  # Enter with decode image
                editable_message[cursor_y]["text"] = (
                    editable_message[cursor_y]["text"][:cursor_x]
                    + key
                    + editable_message[cursor_y]["text"][cursor_x:]
                )
            cursor_x += 1
        elif key == "\x1b":  # Esc退出
            if not is_edit:
                break
            is_edit = False
            if editable_message[cursor_y]["type"] == "image" and editable_message[
                cursor_y
            ].get(
                "changing", False
            ):  # Enter with decode image
                try:
                    editable_message[cursor_y][
                        "text"
                    ] = f"data:image/jpeg;base64,{encode_image(editable_message[cursor_y]['text'].strip())}"
                    editable_message[cursor_y]["changing"] = False
                except Exception as err:
                    editable_message[cursor_y]["text"] = err
        elif key == "\xe0":  # Arrow keys
            key = msvcrt.getwch()
            if is_edit:
                if key == "K":  # Left
                    cursor_x = max(0, cursor_x - 1)
                elif key == "M":  # Right
                    cursor_x = min(
                        len(editable_message[cursor_y]["text"]), cursor_x + 1
                    )
            else:
                if key == "H":  # Up
                    for index, row in enumerate(reversed(editable_message)):
                        if (
                            len(editable_message) - 1 - index < cursor_y
                            and row["selectable"]
                        ):
                            cursor_y = max(0, len(editable_message) - 1 - index)
                            break
                elif key == "P":  # Down
                    for index, row in enumerate(editable_message):
                        if index > cursor_y and row["selectable"]:
                            cursor_y = min(len(editable_message) - 1, index)
                            break

        elif key == "\b" and is_edit:
            if cursor_x > 0:
                cursor_x -= 1
                editable_message[cursor_y]["text"] = (
                    editable_message[cursor_y]["text"][:cursor_x]
                    + editable_message[cursor_y]["text"][cursor_x + 1 :]
                )
            # elif cursor_y > 0:
            #    cursor_x = len(editable_message[cursor_y - 1])
            #    editable_message[cursor_y - 1]["text"] += editable_message[cursor_y][
            #        "text"
            #    ]
            #    del editable_message[cursor_y]
            #    cursor_y -= 1
        elif is_edit:
            editable_message[cursor_y]["text"] = (
                editable_message[cursor_y]["text"][:cursor_x]
                + key
                + editable_message[cursor_y]["text"][cursor_x:]
            )
            cursor_x += 1
    sendable_messages = []
    questions = {}
    try:
        editable_generator = (editable for editable in editable_message)
        editable = next(editable_generator)
        while True:
            if editable["text"].startswith("你：") and not editable["selectable"]:
                editable = next(editable_generator)
                if editable["type"] == "text":
                    question = {
                        "role": "user",
                        "content": [{"type": "text", "text": editable["text"]}],
                    }
                    editable = next(editable_generator)
                elif editable["type"] == "image":
                    question["content"].append(
                        {"type": "image_url", "image_url": {"url": editable["text"]}}
                    )
                    editable = next(editable_generator)
                questions = question.copy()
            if editable["text"].startswith("VLM：") and not editable["selectable"]:
                sendable_messages.append(questions)
                editable = next(editable_generator)
                answer = {
                    "role": "assistant",
                    "content": editable["text"],
                }
                sendable_messages.append(answer)
                editable = next(editable_generator)
    except StopIteration:
        messages[:] = sendable_messages


if __name__ == "__main__":
    while True:
        try:
            option = input(
                "1.重置对话 2.高级选项 3.创建固有Prompt 4.切换端口 5.DEBUG 6.更改对话 7.退出 [键入Enter以对话]"
            )
            base_url = f"{base_url.rsplit(':',1)[0]}:{port}"
            match option:
                case "1":
                    clean_conversation()
                case "2":
                    console_advanced_options()
                case "3":
                    create_inherence_prompt()
                case "4":
                    change_port()
                case "5":
                    debug()
                case "6":
                    change_conversation()
                case "7":
                    break
                case _:
                    simple_image_chat(
                        use_stream=stream,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        top_p=top_p,
                    )
                    if log:
                        with open("log.txt", "wt", encoding="utf8") as f:
                            f.write(str(messages))
        except Exception as err:
            print(f"Error: {err}")
            continue
