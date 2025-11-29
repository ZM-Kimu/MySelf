import os
import socket
import threading

from flask import Flask, jsonify

HOST = "0.0.0.0"
SOCK_PORT = 19198
API_PORT = 36436
doc_folder_path = "questions"
clients: list[socket.socket] = []

app = Flask(__name__)


@app.route("/api/get_questions", methods=["GET"])
def get_questions():
    questions_data = []
    try:
        for f_name in os.listdir(doc_folder_path):
            f_path = os.path.join(doc_folder_path, f_name)
            pure_f_name = os.path.splitext(f_name)[0]

            if os.path.isfile(f_path) and f_path.endswith(".txt"):
                with open(f_path, "r", encoding="utf8") as f:
                    questions_data.append(
                        {"file_name": pure_f_name, "questions": f.read()}
                    )
        return jsonify(
            {
                "success": True,
                "msg": "ok",
                "data": {"questions": questions_data},
            }
        )
    except Exception as e:
        return jsonify({"success": False, "msg": str(e)}), 500


def broadcast(message, sender_sock) -> None:
    for client in clients.copy():
        if client != sender_sock:
            try:
                client.sendall(message)
            except:
                clients.remove(client)


def handle_client(client_socket, addr) -> None:
    print(f"新客户端连接：{addr}")
    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break
            if (d_msg := msg.decode("utf-8", "surrogatepass")).startswith("1919/"):
                target_ip = d_msg.strip().split(" ")[-1]
                kick_client_by_ip(target_ip, client_socket)
                continue
            broadcast(msg, client_socket)
        except:
            break
    print(f"客户端断开：{addr}")
    if client_socket in clients:
        client_socket.close()
        clients.remove(client_socket)


def kick_client_by_ip(target_ip: str, from_sock: socket.socket) -> None:
    for sock in clients.copy():
        if sock.getpeername()[0] == target_ip:
            try:
                sock.sendall("⚠️ 你已被踢出聊天室。".encode())
                sock.close()
                broadcast(f"🚫 来自 {target_ip} 的用户被踢出。".encode(), from_sock)
                print(f"管理员踢出 {target_ip}")
                clients.remove(sock)
            except:
                pass


def run_api_server() -> None:
    app.run(HOST, API_PORT)


def main() -> None:
    threading.Thread(target=run_api_server, daemon=True).start()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, SOCK_PORT))
    server.listen()
    print(f"服务器已启动，监听端口 {SOCK_PORT}...")

    while True:
        client_sock, addr = server.accept()
        clients.append(client_sock)
        thread = threading.Thread(target=handle_client, args=(client_sock, addr))
        thread.start()


if __name__ == "__main__":
    main()
