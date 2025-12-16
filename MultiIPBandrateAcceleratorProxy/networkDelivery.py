import multiprocessing
import socket
import subprocess
import winreg as reg
from multiprocessing.dummy import Pool as ThreadPool

import ping3
import psutil

try:
    multiprocessing.freeze_support()
    multiprocessing.set_start_method("spawn")
except:
    pass


def ping_host(ip):
    try:
        response = ping3.ping(ip, timeout=0.5)
        return (ip, response if not None else False)
    except:
        return (ip, False)


def get_subnet():
    addrs = psutil.net_if_addrs()
    for adapter, addr_info in addrs.items():
        for addr in addr_info:
            if addr.family == socket.AF_INET and not addr.address.startswith("169"):
                ip_addr = addr.address
                netmask = addr.netmask
                return adapter, ip_addr, netmask


def ping_subnet(ips):
    with ThreadPool(processes=50) as pool:
        results = pool.map(ping_host, ips)
        return [ip if alive else None for ip, alive in results]


def set_http_proxy(port):
    key = reg.HKEY_CURRENT_USER
    internet_settings = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
    # 打开注册表键
    reg_key = reg.OpenKey(key, internet_settings, 0, reg.KEY_WRITE)
    # 设置代理服务器
    proxy_server = f"127.0.0.1:{port}"
    reg.SetValueEx(reg_key, "ProxyServer", 0, reg.REG_SZ, proxy_server)
    reg.SetValueEx(reg_key, "ProxyEnable", 0, reg.REG_DWORD, 1)
    reg.CloseKey(reg_key)


def disable_http_proxy():
    key = reg.HKEY_CURRENT_USER
    internet_settings = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
    # 打开注册表键
    reg_key = reg.OpenKey(key, internet_settings, 0, reg.KEY_WRITE)
    # 禁用代理服务器
    reg.SetValueEx(reg_key, "ProxyEnable", 0, reg.REG_DWORD, 0)
    reg.CloseKey(reg_key)


def set_socks_proxy(port):
    key = reg.HKEY_CURRENT_USER
    internet_settings = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
    # 打开注册表键
    reg_key = reg.OpenKey(key, internet_settings, 0, reg.KEY_WRITE)
    # 设置SOCKS代理
    reg.SetValueEx(reg_key, "ProxyServer", 0, reg.REG_SZ, f"socks=127.0.0.1:{port}")
    reg.SetValueEx(reg_key, "ProxyEnable", 0, reg.REG_DWORD, 1)
    reg.CloseKey(reg_key)


def disable_socks_proxy():
    key = reg.HKEY_CURRENT_USER
    internet_settings = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
    # 打开注册表键
    reg_key = reg.OpenKey(key, internet_settings, 0, reg.KEY_WRITE)
    # 禁用代理
    reg.SetValueEx(reg_key, "ProxyEnable", 0, reg.REG_DWORD, 0)
    reg.CloseKey(reg_key)


def set_ip_address(adapter, ips):
    for ip in ips:
        # 添加IP地址
        add_ip_command = f'netsh interface ip add address name="{adapter}" address={ip} mask=255.255.255.0'
        result = subprocess.run(add_ip_command, shell=True, text=True, encoding="utf-8")
        if result.returncode != 0:
            return result.stderr
    return True


def delete_ip_address(adapter, ips):
    for ip in ips:
        try:
            # 添加IP地址
            add_ip_command = (
                f'netsh interface ip delete address name="{adapter}" address={ip}'
            )
            result = subprocess.run(
                add_ip_command, shell=True, capture_output=True, text=True
            )
            if result.returncode != 0:
                return result.stderr
        except Exception as err:
            return err
    return True


def get_available_ip():
    adapter, ip, _ = get_subnet()
    subnet = ip.rsplit(".", 1)[0]
    ips = [f"{subnet}.{i}" for i in range(1, 255)]
    count = 0
    while count < 2:
        results = ping_subnet(ips)
        for ip in results:
            if ip:
                ips.remove(ip)
                count = 0
        count += 1
    return ips, adapter


if __name__ == "__main__":
    get_available_ip()
