from __future__ import annotations

import argparse
import base64
import datetime
import io
import json
import logging
import os
import shutil
import subprocess
import sys
import zipfile
from datetime import timezone
from hashlib import md5
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID
from tencentcloud.common import credential
from tencentcloud.ssl.v20191205 import models
from tencentcloud.ssl.v20191205.ssl_client import SslClient

# ---------- 日志 ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("tencent-ssl-sync")


# ---------- 命令行参数 ----------
def parse_args():
    parser = argparse.ArgumentParser(
        description="从腾讯云同步一个域名的证书到本地 Nginx"
    )
    parser.add_argument(
        "--domain",
        required=True,
        help="要更新证书的域名，例如：example.com",
    )
    parser.add_argument(
        "--fullchain",
        required=True,
        help="本地 fullchain 证书文件路径，例如：/etc/nginx/ssl/example.com/fullchain.crt",
    )
    parser.add_argument(
        "--key",
        required=True,
        help="本地私钥文件路径，例如：/etc/nginx/ssl/example.com/example.com.key",
    )
    parser.add_argument(
        "--search-key",
        dest="search_key",
        help="在腾讯云证书池中查询用的关键词，默认等于 --domain",
    )
    parser.add_argument(
        "--nginx-test-cmd",
        default="nginx -t",
        help='测试 Nginx 配置的命令，默认："nginx -t"',
    )
    parser.add_argument(
        "--nginx-reload-cmd",
        default="systemctl reload nginx",
        help='重载 Nginx 的命令，默认："systemctl reload nginx"',
    )
    parser.add_argument(
        "--no-prefer-nginx-bundle",
        action="store_true",
        help="不要优先使用 ZIP 中的 Nginx 专用 fullchain/bundle 文件",
    )
    parser.add_argument(
        "--keep-local-key",
        action="store_true",
        help="即使 ZIP 内提供了私钥，也始终保留本地原有私钥",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只检查与日志输出，不写入证书/私钥，也不重载 Nginx",
    )
    return parser.parse_args()


# ---------- 工具函数 ----------
def ssl_client_new(SID: str, SKEY: str) -> SslClient:
    cred = credential.Credential(SID, SKEY)
    return SslClient(cred, "")


def parse_time(s: str) -> datetime.datetime:
    """腾讯云 API 返回 'YYYY-MM-DD HH:MM:SS'"""
    return (
        datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
        if s
        else datetime.datetime.min
    )


def _first_leaf_from_fullchain(pem: bytes) -> bytes:
    """从 fullchain 中取第一张 leaf 证书"""
    end_marker = b"-----END CERTIFICATE-----"
    idx = pem.find(end_marker)
    if idx == -1:
        raise ValueError("invalid PEM: END CERTIFICATE not found")
    return pem[: idx + len(end_marker)] + b"\n"


def san_dns_from_pem(pem_bytes: bytes) -> list[str]:
    """返回证书 SAN 里的所有 DNSName（小写）。若无 SAN，回退到 CN。"""
    cert = x509.load_pem_x509_certificate(pem_bytes, default_backend())
    try:
        san = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
        return [d.lower() for d in san.value.get_values_for_type(x509.DNSName)]
    except x509.ExtensionNotFound:
        # 没有 SAN 就回退到 CN
        try:
            cn = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
            return [cn.lower()]
        except Exception:
            return []


def dns_match(host: str, pattern: str) -> bool:
    """
    规则：
      - 精确匹配：pattern == host
      - 单层通配：*.example.com 仅匹配 a.example.com，
        不匹配 a.b.example.com，也不匹配 example.com
    """
    host = host.lower().rstrip(".")
    pattern = pattern.lower().rstrip(".")
    if pattern == host:
        return True
    if pattern.startswith("*."):
        base = pattern[2:]  # "example.com"
        return host.endswith("." + base) and host.count(".") == base.count(".") + 1
    return False


def cert_covers_domain(fullchain: bytes, wanted: str) -> bool:
    """fullchain 是否覆盖 wanted 这个域名"""
    try:
        leaf = _first_leaf_from_fullchain(fullchain)
        sans = san_dns_from_pem(leaf)
        return any(dns_match(wanted, san) for san in sans)
    except Exception:
        return False


def download_cert_zip(cli: SslClient, cert_id: str) -> bytes:
    req = models.DownloadCertificateRequest()
    req.CertificateId = cert_id
    rsp = cli.DownloadCertificate(req)
    content = rsp.Content or ""
    if not content:
        raise RuntimeError(f"证书 {cert_id} 无可下载内容（可能未允许下载或状态不对）")
    return base64.b64decode(content)


def extract_nginx_materials(zip_bytes: bytes, prefer_nginx_bundle: bool):
    """
    返回 (fullchain_pem_bytes, private_key_candidates)
    - 优先寻找 NGINX 专用 bundle/fullchain
    - 否则从 certificate + ca_bundle 组合 fullchain
    """
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        files = {
            name: zf.read(name) for name in zf.namelist() if not name.endswith("/")
        }

    def find(names) -> bytes | None:
        for n in files:
            lower = n.lower()
            if any(lower.endswith(x) for x in names):
                return files[n]
        return None

    def find_all(names) -> list[bytes]:
        hits: list[bytes] = []
        for n in files:
            lower = n.lower()
            if any(lower.endswith(x) for x in names):
                hits.append(files[n])
        return hits

    key_candidates = find_all([".key"])

    # 尝试直接找到 fullchain/bundle
    if prefer_nginx_bundle:
        fullchain = None
        for cand in ["fullchain.pem", "fullchain.crt", "bundle.pem", "bundle.crt"]:
            b = find([cand])
            if b:
                fullchain = b
                break
        if fullchain:
            return fullchain, key_candidates

    # 拼接 fullchain：leaf + ca_bundle
    leaf = find(["certificate.pem", "certificate.crt", "server.crt"])
    cabundle = find(["ca_bundle.pem", "ca_bundle.crt"])
    if not leaf:
        # 兜底：找第一个 .crt/.pem 当 leaf
        leaf = find([".crt", ".pem"])
    if not leaf:
        raise RuntimeError("未在 ZIP 中找到证书文件")
    fullchain = leaf + (cabundle or b"")
    return fullchain, key_candidates


def select_matching_key(fullchain: bytes, key_candidates: list[bytes]) -> bytes | None:
    if not key_candidates:
        return None
    try:
        md5_cert = cert_pubkey_md5(_first_leaf_from_fullchain(fullchain))
    except Exception:
        return None
    for key_bytes in key_candidates:
        try:
            if key_pubkey_md5(key_bytes) == md5_cert:
                return key_bytes
        except Exception:
            continue
    return None


def find_latest_matching_cert(
    cli: SslClient,
    search_key: str,
    wanted_domain: str,
    prefer_nginx_bundle: bool,
):
    """
    用 search_key 在云端查找证书池，逐个下载校验，
    返回一张可以覆盖 wanted_domain 的“最新”证书元信息。
    """
    offset = 0
    limit = 100

    while True:
        req = models.DescribeCertificatesRequest()
        params = {
            "SearchKey": search_key,  # 做初筛（模糊匹配）
            "CertificateType": "SVR",
            "CertificateStatus": [1],  # 已签发
            "ExpirationSort": "DESC",
            "Limit": limit,
            "Offset": offset,
        }
        req.from_json_string(json.dumps(params))
        rsp = cli.DescribeCertificates(req)
        if not rsp or not rsp.Certificates:
            return None

        for c in rsp.Certificates:
            # 下载 -> 提取 fullchain -> 校验是否覆盖 wanted_domain
            try:
                zip_bytes = download_cert_zip(cli, c.CertificateId)
                fullchain, key_candidates = extract_nginx_materials(
                    zip_bytes, prefer_nginx_bundle
                )
            except Exception as e:
                logger.warning(
                    "下载或解析证书 %s 失败，将尝试下一张：%s",
                    getattr(c, "CertificateId", "?"),
                    e,
                )
                continue

            if not cert_covers_domain(fullchain, wanted_domain):
                continue

            key_bytes = select_matching_key(fullchain, key_candidates)
            zip_key_present = bool(key_candidates)
            zip_key_matched = key_bytes is not None
            if zip_key_present and not zip_key_matched:
                logger.warning(
                    "证书 %s ZIP 内存在私钥，但都与证书不匹配，将忽略 ZIP 私钥",
                    getattr(c, "CertificateId", "?"),
                )

            return {
                "id": c.CertificateId,
                "end": parse_time(c.CertEndTime),
                "fullchain": fullchain,
                "key_bytes": key_bytes,
                "zip_key_present": zip_key_present,
                "zip_key_matched": zip_key_matched,
            }

        if len(rsp.Certificates) < limit:
            return None
        offset += limit


def read_local_notafter(fullchain_path: str) -> datetime.datetime:
    """读取本地 fullchain 第一张证书的 NotAfter 时间"""
    p = Path(fullchain_path)
    if not p.exists():
        return datetime.datetime.min
    data = p.read_bytes()
    first = _first_leaf_from_fullchain(data)
    cert = x509.load_pem_x509_certificate(first, default_backend())
    # cryptography 42+ 提供 not_valid_after_utc；老版本回退
    try:
        dt = cert.not_valid_after_utc  # tz-aware
    except AttributeError:
        dt = cert.not_valid_after  # naive，将来会被移除
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
    return dt.replace(tzinfo=None)


def cert_pubkey_md5(pem_bytes: bytes) -> str:
    cert = x509.load_pem_x509_certificate(pem_bytes, default_backend())
    pub = cert.public_key().public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return md5(pub).hexdigest()


def key_pubkey_md5(key_bytes: bytes) -> str:
    key = serialization.load_pem_private_key(
        key_bytes, password=None, backend=default_backend()
    )
    pub = key.public_key().public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    return md5(pub).hexdigest()


def atomic_install(
    domain: str,
    fullchain_path: str,
    key_path: str,
    new_fullchain: bytes,
    new_key: bytes | None,
    dry_run: bool = False,
) -> None:
    """原子性地部署证书和私钥，失败会保留备份；dry_run 时不实际写入"""
    live_full = Path(fullchain_path)
    live_key = Path(key_path)
    live_dir = live_full.parent
    backup_dir = live_dir / "backup"
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    # 若没有新 key，就读取现有 key
    if new_key is None:
        if not live_key.exists():
            raise RuntimeError("平台未提供私钥，而本机也不存在旧私钥，无法部署")
        new_key = live_key.read_bytes()

    # 匹配校验（证书 vs 私钥）
    md5_cert = cert_pubkey_md5(_first_leaf_from_fullchain(new_fullchain))
    md5_key = key_pubkey_md5(new_key)
    if md5_cert != md5_key:
        raise RuntimeError("证书与私钥不匹配，请确认是否使用了新 CSR/新私钥")

    if dry_run:
        logger.info(
            "[%s] dry-run：已校验证书与私钥匹配，不写入文件",
            domain,
        )
        return

    # 真正写入
    live_dir.mkdir(parents=True, exist_ok=True)
    backup_dir.mkdir(exist_ok=True)

    # 备份
    if live_full.exists():
        shutil.copy2(live_full, backup_dir / f"{live_full.name}.{ts}")
    if live_key.exists():
        shutil.copy2(live_key, backup_dir / f"{live_key.name}.{ts}")

    # 写入（权限）
    tmp_full = live_dir / f".{live_full.name}.tmp"
    tmp_key = live_dir / f".{live_key.name}.tmp"
    tmp_full.write_bytes(new_fullchain)
    os.chmod(tmp_full, 0o644)
    tmp_key.write_bytes(new_key)
    os.chmod(tmp_key, 0o600)

    # 原子替换
    tmp_full.replace(live_full)
    tmp_key.replace(live_key)


def nginx_reload(test_cmd: str, reload_cmd: str, dry_run: bool = False):
    """先测试配置，再重载 Nginx；dry-run 时只测试不重载"""

    def run(cmd):
        subprocess.run(cmd, shell=True, check=True)

    # 先测试配置
    run(test_cmd)

    if dry_run:
        logger.info("dry-run：已通过 nginx -t 检测，不执行重载")
        return

    run(reload_cmd)


# ---------- 主流程 ----------
def main() -> int:
    args = parse_args()

    SID = os.environ.get("TENCENTCLOUD_SECRET_ID")
    SKEY = os.environ.get("TENCENTCLOUD_SECRET_KEY")
    if not SID or not SKEY:
        logger.error(
            "请通过环境变量设置 TENCENTCLOUD_SECRET_ID / TENCENTCLOUD_SECRET_KEY"
        )
        return 2

    cli = ssl_client_new(SID, SKEY)

    domain = args.domain
    fullchain_path = args.fullchain
    key_path = args.key
    search_key = args.search_key or domain
    prefer_nginx_bundle = not args.no_prefer_nginx_bundle
    replace_key_if_zip_provides = not args.keep_local_key

    # 读取本地证书到期时间（不存在则视为最早）
    try:
        local_end = read_local_notafter(fullchain_path)
    except Exception as e:
        logger.exception("[%s] 读取本地证书失败：%s", domain, e)
        return 1

    # 查询远端证书
    remote = find_latest_matching_cert(
        cli,
        search_key=search_key,
        wanted_domain=domain,
        prefer_nginx_bundle=prefer_nginx_bundle,
    )

    if not remote:
        logger.warning("[%s] 未找到可覆盖该域名的已签发证书，退出", domain)
        return 0

    logger.info(
        "[%s] 本地到期: %s；云端最新到期: %s (ID=%s)",
        domain,
        local_end,
        remote["end"],
        remote["id"],
    )
    if remote["end"] <= local_end:
        logger.info("[%s] 已是最新或更新无必要，退出", domain)
        return 0

    fullchain, key_bytes = remote["fullchain"], remote["key_bytes"]
    zip_key_present = remote.get("zip_key_present", False)
    zip_key_matched = remote.get("zip_key_matched", False)

    # 终极保险：再校验一次（理论上已通过）
    if not cert_covers_domain(fullchain, domain):
        logger.error("[%s] 警告：下载的证书不覆盖该域名（中止）", domain)
        return 1

    # 私钥替换逻辑
    if key_bytes is None:
        if zip_key_present and not zip_key_matched:
            logger.warning("[%s] ZIP 私钥与证书不匹配，将沿用本机现有私钥", domain)
        else:
            logger.info("[%s] ZIP 未提供私钥，将沿用本机现有私钥", domain)
    else:
        if not replace_key_if_zip_provides:
            logger.info("[%s] 已禁用替换私钥，仍沿用本机现有私钥", domain)
            key_bytes = None
        # 否则就使用 zip 中的新私钥

    # 部署证书
    try:
        atomic_install(
            domain=domain,
            fullchain_path=fullchain_path,
            key_path=key_path,
            new_fullchain=fullchain,
            new_key=key_bytes,
            dry_run=args.dry_run,
        )
    except Exception as e:
        logger.exception("[%s] 部署证书失败：%s", domain, e)
        return 1

    # 重载 Nginx
    try:
        nginx_reload(
            test_cmd=args.nginx_test_cmd,
            reload_cmd=args.nginx_reload_cmd,
            dry_run=args.dry_run,
        )
    except Exception as e:
        logger.exception("[%s] 证书已部署，但 Nginx 重载失败：%s", domain, e)
        return 1

    if args.dry_run:
        logger.info("[%s] dry-run：模拟更新成功", domain)
    else:
        logger.info("[%s] 证书更新并重载 Nginx 成功", domain)
    return 0


if __name__ == "__main__":
    sys.exit(main())
