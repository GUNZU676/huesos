import subprocess
import os
import json
import sys

# Конфиг VPN
config = {
    "server": "0.0.0.0",
    "server_port": 8388,
    "password": "MyVpn2024Pass",  # Поменяй на свой пароль!
    "timeout": 300,
    "method": "aes-256-cfb"
}

# Сохраняем конфиг
with open("/app/config.json", "w") as f:
    json.dump(config, f)

# Путь к ssserver
ssserver_path = os.path.expanduser("~/.local/bin/ssserver")
if not os.path.exists(ssserver_path):
    ssserver_path = "/app/.local/bin/ssserver"

try:
    os.chmod(ssserver_path, 0o755)
except:
    pass

# Запускаем VPN
print("🚀 Shadowsocks VPN запущен на порту 8388")
subprocess.run([ssserver_path, "-c", "/app/config.json"])
