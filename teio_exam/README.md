# 帝王题目检索器（作弊器）

PyQt5 桌面小工具，用于本地/远端题库检索与内置简易聊天室，支持题目图片展示、正则/普通搜索、高亮跳转和鼠标手势控制。

## 功能概览
- 题库获取：从 `questions/*.txt` 或远端 `http://<host>:36436/api/get_questions` 拉取题目，自动解析内嵌的 base64 图片标记 `<!image!>...<¡ǝƃɐɯı¡>` 并展示。
- 搜索与高亮：支持普通/正则检索、查找下一个、状态指示 `当前/总数`，搜索仅作用于纯文本内容。
- UI 控制：无边框可拖拽/缩放，置顶切换，极简模式，主窗+聊天窗联动移动。
- 交互快捷方式：
  - 中键：置顶/取消置顶
  - 右键：窗口移动到鼠标位置
  - 鼠标手势：上上下下左左右右 → 隐藏/显示；上下上下 → 极简模式；剪贴板监听自动搜索（复制即搜）
- 聊天室：内置 TCP 客户端，尝试主/备/公网三组 IP，支持管理员踢人指令，昵称修改。
- 服务器端：Flask API 提供题库，TCP 聊天广播，支持踢出指定 IP。

## 目录速览
- `main.py`：应用入口（单实例保护）。
- `src/main_window.py`：主界面、搜索逻辑、手势/剪贴板监听。
- `src/search_engine.py`：文本搜索与高亮。
- `src/image_processor.py`：题目内容中的图片解析与插入。
- `src/chat_window.py` / `src/chat_server.py`：聊天 UI + TCP 客户端。
- `src/api_client.py`：远端题库拉取。
- `src/window_manager.py`：置顶与全局鼠标事件。
- `exam_server.py`：题库+聊天服务端。
- `document_extractor.py`：docx/pdf 转 txt，保留表格、嵌入图片。
- `questions/`：题库源文件（txt/docx/pdf）。

## 环境准备
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## 配置与定制
- 题库服务端（`exam_server.py`）：默认读取 `questions/` 下的 txt 作为题库，端口 `API_PORT=36436`、`SOCK_PORT=19198`。如需更改端口或题库目录，修改文件顶部常量后重启。
- 客户端 API 目标（`src/api_client.py`）：默认 `host=localhost`、`port=36436`。部署到局域网/公网时，将 `host` 改为服务器 IP，或在实例化后赋值 `api_client.host`/`port`。
- 聊天服务器地址（`src/chat_server.py`）：`MAIN_SERVER` / `BACKUP_SERVER` / `PUB_SERVER` 目前占位为 `0.0.0.0`，请改成实际 IP；端口由 `COM_PORT` 控制。
- 管理代号（`src/utils.py`）：`ADMIN_CODES` / `SUPER_ADMIN_CODE` 为明文管理口令，如需替换请同步告知使用者。
- 打包权限（`teio_exam.spec`）：默认 `uac_admin=True` 以管理员权限运行，可按需改为 `False`。
- 可选 OCR：`requirements.txt` 包含 `paddleocr`、`mss` 等依赖，若不使用 OCR 可移除以减轻体积；对应代码在 `src/ocr_capture.py`（默认注释）。

## 置顶说明
- 功能：通过 `TopmostWidget` 定时维持窗口置顶，避免被其他窗口遮挡；
- 开关：鼠标中键点击主窗口可切换置顶；隐藏/极简模式会自动调整置顶状态。
- 入口代码：`src/window_manager.py`（置顶逻辑）、`src/main_window.py`（绑定中键/手势）。如需关闭强制置顶，可将 `TopmostWidget.enforce_topmost_forever` 的调用注释或在界面上中键切换。

## 运行
### 启动服务器（题库 API + 聊天）
```bash
python exam_server.py
# API:  http://<server_ip>:36436/api/get_questions
# Chat: TCP 19198
```

### 启动客户端
```bash
python main.py
```
- “获取题目”按钮：首次从服务器拉取题库并循环切换。
- 搜索框：输入关键词后回车普通搜，“正则搜”按钮开启正则。
- 剪贴板搜：复制文本即自动搜索。
- “猴子”按钮：输入管理代号后点击打开聊天室；再次点击关闭。管理员代号见 `src/utils.py::AppConstants.ADMIN_CODES`（超级管理员同 `SUPER_ADMIN_CODE`）。

### 打包
```bash
pyinstaller teio_exam.spec
```

## 聊天室说明
- 连接顺序：主服务器 → 备用 → 公网（端口 19198）。
- 消息格式自动包含时间/IP/昵称；管理员附带“📍管理员📍”标记。
- 踢人：管理员在输入框输入目标 IP，点击“踢”，发送 `1919/kick <ip>`。

## 题库文件格式
- 文本：UTF-8，每行一条/多条题目内容。
- 图片：在文本中用 `<!image!>{base64}<¡ǝƃɐɯı¡>` 包裹，客户端会渲染为图片并维持搜索映射。
- 表格：`document_extractor.py` 会扁平化输出为“表格-<序号>”文本。

## 已知可选能力
- OCR 截图搜索（`src/ocr_capture.py`）已留代码但默认关闭，需 PaddleOCR 等依赖并启用后才可使用。

## 常见问题
- 置顶/前置失败：可能被系统阻止，日志会打印警告。
- 正则无效：表达式错误会自动降级为普通搜索。
- 连接服务器失败：确认 API/Chat 端口、防火墙、IP 填写正确；可在聊天窗内查看当前连接提示。
