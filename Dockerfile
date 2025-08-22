FROM ubuntu:22.04

# 安装必要的依赖包
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 \
    python3-uvloop \
    python3-cryptography \
    python3-socks \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 创建用户并同时创建家目录
RUN useradd -m -u 10000 tgproxy

# 设置工作目录
WORKDIR /home/tgproxy/

# 复制文件并设置权限
COPY --chown=tgproxy:tgproxy mtprotoproxy.py config.py ./

# 切换到非root用户
USER tgproxy

# 容器启动命令
CMD ["python3", "mtprotoproxy.py"]
