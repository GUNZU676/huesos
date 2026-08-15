FROM ghcr.io/shadowsocks/ssserver-rust:latest

ENV NO_PROXY=

# Копируем конфиг поверх стандартного
COPY config.json /etc/shadowsocks-rust/config.json

# Запускаем с правильным конфигом
CMD ["ssserver", "-c", "/etc/shadowsocks-rust/config.json"]
