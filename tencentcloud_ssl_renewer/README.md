# tencentcloud_ssl_renewer

用于从腾讯云证书池同步指定域名的最新已签发证书到本地 Nginx，并在必要时自动重载 Nginx。

## 依赖
- Python 3.9+
- tencentcloud-sdk-python
- cryptography

依赖见 `requirements.txt`。

## 环境变量
运行前需要设置腾讯云 API 凭证：

```
export TENCENTCLOUD_SECRET_ID=xxxx
export TENCENTCLOUD_SECRET_KEY=yyyy
```

## 直接使用 main.py
建议先 dry-run 验证流程无误：

```
python main.py --domain example.com \
  --fullchain /etc/nginx/ssl/example.com/fullchain.crt \
  --key /etc/nginx/ssl/example.com/example.com.key \
  --dry-run
```

确认无误后去掉 `--dry-run`。

常用参数：
- `--search-key`：证书池查询关键字（默认等于 `--domain`）
- `--no-prefer-nginx-bundle`：不优先使用 ZIP 中的 Nginx bundle/fullchain
- `--keep-local-key`：即使 ZIP 提供私钥，也保留本地私钥
- `--nginx-test-cmd`：配置测试命令
- `--nginx-reload-cmd`：配置重载命令
- `--result-file`：将执行结果写入文件（`updated`/`noop`/`would_update`/`error`）

## 使用 manager.sh（推荐）
`manager.sh` 提供配置管理与定时更新能力，会自动创建 venv 并安装依赖。

- 添加/更新一个证书配置并立即部署：

```
./manager.sh add example.com \
  /etc/nginx/ssl/example.com/fullchain.crt \
  /etc/nginx/ssl/example.com/example.com.key
```

- 添加/更新一个证书配置，并在证书“实际更新成功”后执行命令：

```
./manager.sh add xxx.aa.com \
  /etc/nginx/ssl/xxx.aa.com/fullchain.crt \
  /etc/nginx/ssl/xxx.aa.com/xxx.aa.com.key \
  --post-cmd "docker restart xxx_nginx"
```

- 添加/更新一个证书配置，并在证书“实际更新成功”后执行命令：

```
./manager.sh add xxx.aa.com \
  /etc/nginx/ssl/xxx.aa.com/fullchain.crt \
  /etc/nginx/ssl/xxx.aa.com/xxx.aa.com.key \
  --post-cmd "docker restart xxx_nginx"
```

- 列出已配置证书：

```
./manager.sh list
```

- 批量更新（支持 dry-run）：

```
./manager.sh renew
./manager.sh renew --dry-run
```

- 安装 cron 定时任务（每天 03:00）：

```
sudo ./manager.sh install-cron
```

配置文件默认在 `/etc/tencent-ssl-sync.conf`，格式为：

```
<domain>|<fullchain>|<key>|<post_cmd(可选)>
<domain>|<fullchain>|<key>|<post_cmd(可选)>
```

`post_cmd` 仅在该域名证书“实际更新成功”后执行；`renew --dry-run` 只会提示将执行的命令，不会真正执行。

`post_cmd` 仅在该域名证书“实际更新成功”后执行；`renew --dry-run` 只会提示将执行的命令，不会真正执行。

## 行为说明
- 仅在云端证书到期时间晚于本地证书时才会更新。
- 云端 `CertEndTime` 按 GMT+8 解析后换算为 UTC 进行比较。
- 证书部署为原子写入，旧文件会备份到 `fullchain` 所在目录的 `backup/` 下。
- 需要具备写证书目录与重载 Nginx 的权限（通常需要 root）。
