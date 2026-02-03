#!/usr/bin/env bash
set -euo pipefail

# ========== 基本配置 ==========
# Python 脚本路径（默认与本 bash 同目录）
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="$SCRIPT_DIR/main.py"

# 配置文件：记录所有证书
CONF_FILE="/etc/tencent-ssl-sync.conf"
# 日志文件：cron 自动 renew 的输出
LOG_FILE="/var/log/tencent-ssl-sync.log"

# 虚拟环境目录（默认在脚本同目录下）
VENV_DIR="${VENV_DIR:-$SCRIPT_DIR/.venv}"
VENV_PY="$VENV_DIR/bin/python"

# Python 可执行文件
# - 若外部显式设置了 PYTHON_BIN，则使用外部的（不会自动建 venv）
# - 否则使用 venv 里的 python，并自动创建 venv + 安装依赖
PYTHON_BIN="${PYTHON_BIN:-$VENV_PY}"

# ========== 工具函数 ==========
usage() {
  cat <<EOF
用法: $0 <命令> [参数...]

命令：
  add <domain> <fullchain> <key> [--post-cmd "<cmd>"]
      添加/更新一个证书配置，并立刻执行一次部署。
      例：
        $0 add xxx.com \\
            /etc/nginx/ssl/xxx.com_nginx/xxx.com_bundle.crt \\
            /etc/nginx/ssl/xxx.com_nginx/xxx.com.key
      可选：
        --post-cmd "<cmd>"  在该域名证书“实际更新成功”后执行命令
      例：
        $0 add xxx.aa.com \\
            /etc/nginx/ssl/xxx.aa.com/fullchain.crt \\
            /etc/nginx/ssl/xxx.aa.com/xxx.aa.com.key \\
            --post-cmd "docker restart xxx_nginx"

  renew [--dry-run]
      对配置文件中的所有证书执行更新。
      --dry-run 只检查，不写文件、不重载 Nginx。

  list
      列出当前已配置的所有证书。

  install-cron
      安装自动续期的 cron 任务（每天 3:00 执行 renew）。
      会把当前环境中的 TENCENTCLOUD_SECRET_ID / KEY 写入 /etc/cron.d/tencent-ssl-sync
      请在执行前先 export 好这两个环境变量。

说明：
  - 本脚本会在首次运行时自动创建虚拟环境：
        $VENV_DIR
    并自动安装所需依赖：
        tencentcloud-sdk-python, cryptography
  - 如需自定义 Python 解释器，可在外部设置环境变量：
        PYTHON_BIN=/path/to/python
    此时将不会自动创建 venv。
  - 需要 root 权限（写 /etc、证书目录、重载 Nginx）
  - Python 脚本默认路径：$PY_SCRIPT
  - 腾讯云凭证通过环境变量提供：
      TENCENTCLOUD_SECRET_ID
      TENCENTCLOUD_SECRET_KEY
EOF
}

ensure_conf() {
  if [[ ! -f "$CONF_FILE" ]]; then
    touch "$CONF_FILE"
    chmod 600 "$CONF_FILE"
  fi
}

check_py_script() {
  if [[ ! -f "$PY_SCRIPT" ]]; then
    echo "ERROR: 找不到 Python 脚本：$PY_SCRIPT" >&2
    echo "请确认 main.py 与本 bash 在同一目录，或手动修改 PY_SCRIPT 变量。" >&2
    exit 1
  fi
}

# 自动创建 venv 并安装依赖（仅在使用默认 VENV_PY 时生效）
ensure_venv() {
  # 若用户手动指定了 PYTHON_BIN（非 venv），则不干预
  if [[ "$PYTHON_BIN" != "$VENV_PY" ]]; then
    return
  fi

  # venv 已存在且 python 可执行
  if [[ -x "$VENV_PY" ]]; then
    return
  fi

  echo "检测到未创建虚拟环境，将自动创建 venv 并安装依赖..."
  echo "  venv 目录：$VENV_DIR"

  local base_python="${BASE_PYTHON:-python3}"
  if ! command -v "$base_python" >/dev/null 2>&1; then
    echo "ERROR: 找不到 Python 解释器：$base_python" >&2
    echo "请安装 python3 或设置 BASE_PYTHON 环境变量，例如：" >&2
    echo "  BASE_PYTHON=/usr/bin/python3 $0 add ..." >&2
    exit 1
  fi

  # 创建 venv
  "$base_python" -m venv "$VENV_DIR"

  # 安装依赖
  "$VENV_PY" -m pip install --upgrade pip
  "$VENV_PY" -m pip install -r requirements.txt

  echo "虚拟环境和依赖已安装完毕。"
}

# $1: domain $2: fullchain $3: key $4: post_cmd(optional)
add_cert() {
  local domain="$1"
  local fullchain="$2"
  local key="$3"
  local post_cmd="${4:-}"

  ensure_conf
  check_py_script
  ensure_venv

  # 创建证书目录
  local dir
  dir="$(dirname "$fullchain")"
  mkdir -p "$dir"

  if [[ "$post_cmd" == *"|"* ]]; then
    echo "ERROR: --post-cmd 不能包含字符 |" >&2
    exit 1
  fi

  # 更新配置文件：去掉旧记录，再追加新记录（格式：domain|fullchain|key|post_cmd）
  local tmp
  tmp="$(mktemp)"
  # 过滤掉旧记录（按第一列精确匹配 domain）
  awk -F'|' -v d="$domain" '$1 != d' "$CONF_FILE" > "$tmp"
  printf '%s|%s|%s|%s\n' "$domain" "$fullchain" "$key" "$post_cmd" >> "$tmp"
  mv "$tmp" "$CONF_FILE"
  chmod 600 "$CONF_FILE"

  echo "已写入配置：$domain -> $fullchain / $key"
  echo "立即执行一次部署..."

  # 调用 Python 执行实际更新
  local result_file
  result_file="$(mktemp)"
  if ! "$PYTHON_BIN" "$PY_SCRIPT" \
    --domain "$domain" \
    --fullchain "$fullchain" \
    --key "$key" \
    --result-file "$result_file"; then
    echo "!!! [$domain] 更新失败" >&2
    rm -f "$result_file"
    exit 1
  fi

  local status
  status="$(cat "$result_file" 2>/dev/null || true)"
  rm -f "$result_file"

  if [[ "$status" == "updated" && -n "${post_cmd// }" ]]; then
    echo "执行 post-cmd: $post_cmd"
    if ! bash -c "$post_cmd"; then
      echo "!!! [$domain] post-cmd 执行失败" >&2
      exit 1
    fi
  fi
}

list_certs() {
  ensure_conf
  if [[ ! -s "$CONF_FILE" ]]; then
    echo "当前还没有任何证书配置～"
    return
  fi

  echo "当前已配置的证书："
  echo "-------------------------------------------"
  while IFS='|' read -r domain fullchain key post_cmd; do
    [[ -z "${domain// }" ]] && continue
    [[ "$domain" =~ ^# ]] && continue
    printf '  domain   : %s\n' "$domain"
    printf '  fullchain: %s\n' "$fullchain"
    printf '  key      : %s\n' "$key"
    if [[ -n "${post_cmd// }" ]]; then
      printf '  post-cmd : %s\n' "$post_cmd"
    fi
    echo "-------------------------------------------"
  done < "$CONF_FILE"
}

# $1: dry_run(true/false)
renew_all() {
  local dry_run="$1"
  ensure_conf
  check_py_script
  ensure_venv

  if [[ ! -s "$CONF_FILE" ]]; then
    echo "没有任何证书配置，跳过 renew。"
    return
  fi

  local extra_arg=""
  if [[ "$dry_run" == "true" ]]; then
    extra_arg="--dry-run"
    echo "以 dry-run 模式对所有证书进行模拟更新..."
  else
    echo "开始对所有证书执行更新..."
  fi

  local any_fail=0

  while IFS='|' read -r domain fullchain key post_cmd; do
    [[ -z "${domain// }" ]] && continue
    [[ "$domain" =~ ^# ]] && continue

    echo "=== [$domain] ==="
    local result_file
    result_file="$(mktemp)"
    if ! "$PYTHON_BIN" "$PY_SCRIPT" \
        --domain "$domain" \
        --fullchain "$fullchain" \
        --key "$key" \
        --result-file "$result_file" \
        $extra_arg; then
      echo "!!! [$domain] 更新失败" >&2
      any_fail=1
      rm -f "$result_file"
    else
      local status
      status="$(cat "$result_file" 2>/dev/null || true)"
      rm -f "$result_file"
      if [[ "$dry_run" == "true" ]]; then
        if [[ "$status" == "would_update" && -n "${post_cmd// }" ]]; then
          echo "dry-run：将执行 post-cmd: $post_cmd"
        fi
      else
        if [[ "$status" == "updated" && -n "${post_cmd// }" ]]; then
          echo "执行 post-cmd: $post_cmd"
          if ! bash -c "$post_cmd"; then
            echo "!!! [$domain] post-cmd 执行失败" >&2
            any_fail=1
          fi
        fi
      fi
    fi
    echo
  done < "$CONF_FILE"

  if [[ "$any_fail" -ne 0 ]]; then
    echo "部分证书更新失败，详情请查看日志。"
    return 1
  else
    echo "所有证书已更新完毕。"
  fi
}

install_cron() {
  # 必须 root
  if [[ "$EUID" -ne 0 ]]; then
    echo "ERROR: 安装 cron 需要 root 权限，请使用 sudo 运行。" >&2
    exit 1
  fi

  local sid="${TENCENTCLOUD_SECRET_ID:-}"
  local skey="${TENCENTCLOUD_SECRET_KEY:-}"
  if [[ -z "$sid" || -z "$skey" ]]; then
    echo "ERROR: 请先在当前 shell 中设置腾讯云环境变量：" >&2
    echo "  export TENCENTCLOUD_SECRET_ID=xxxx" >&2
    echo "  export TENCENTCLOUD_SECRET_KEY=yyyy" >&2
    exit 1
  fi

  # 确保脚本路径是绝对路径
  local script_path
  script_path="$(cd "$SCRIPT_DIR" && pwd)/$(basename "$0")"

  local cron_file="/etc/cron.d/tencent-ssl-sync"
  cat >"$cron_file" <<EOF
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

TENCENTCLOUD_SECRET_ID=$sid
TENCENTCLOUD_SECRET_KEY=$skey

0 3 * * * root $script_path renew >> $LOG_FILE 2>&1
EOF

  chmod 600 "$cron_file"
  echo "已写入 cron 任务：$cron_file"
  echo "  - 每天 03:00 自动执行：$script_path renew"
  echo "  - 腾讯云凭证已写入该文件（仅 root 可读），若后续修改凭证请重新执行 install-cron。"
}

# ========== 主逻辑 ==========
cmd="${1:-}"

case "$cmd" in
  add)
    shift
    if [[ $# -lt 3 ]]; then
      echo "用法: $0 add <domain> <fullchain> <key> [--post-cmd \"<cmd>\"]" >&2
      exit 1
    fi
    domain="$1"
    fullchain="$2"
    key="$3"
    shift 3
    post_cmd=""
    while [[ $# -gt 0 ]]; do
      case "$1" in
        --post-cmd)
          shift
          if [[ $# -eq 0 ]]; then
            echo "ERROR: --post-cmd 需要一个命令字符串" >&2
            exit 1
          fi
          post_cmd="$1"
          ;;
        --post-cmd=*)
          post_cmd="${1#*=}"
          ;;
        *)
          if [[ -z "$post_cmd" ]]; then
            post_cmd="$1"
          else
            echo "未知参数：$1" >&2
            exit 1
          fi
          ;;
      esac
      shift
    done
    add_cert "$domain" "$fullchain" "$key" "$post_cmd"
    ;;
  renew)
    # 支持: renew 或 renew --dry-run
    dry_run="false"
    if [[ "${2:-}" == "--dry-run" ]]; then
      dry_run="true"
    fi
    renew_all "$dry_run"
    ;;
  list)
    list_certs
    ;;
  install-cron)
    install_cron
    ;;
  ""|-h|--help|help)
    usage
    ;;
  *)
    echo "未知命令：$cmd" >&2
    usage
    exit 1
    ;;
esac
