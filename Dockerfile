FROM ghcr.io/shadowsocks/ssserver-rust:latest

ENV NO_PROXY=

# Удаляем стандартный конфиг и кладем свой
RUN rm -f /etc/shadowsocks-rust/config.json
COPY config.json /etc/shadowsocks-rust/config.json

# Запускаем с правильным конфигом
CMD ["ssserver", "-c", "/etc/shadowsocks-rust/config.json"]
