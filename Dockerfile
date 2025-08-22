FROM ubuntu:22.04

# 安装必要的依赖包
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 \
    python3-uvloop \
    python3-cryptography \
    python3-socks \
    libcap2-bin \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 创建用户并同时创建家目录 (-m 参数)
RUN useradd -m -u 10000 tgproxy

# 设置工作目录
WORKDIR /home/tgproxy/

# 先复制文件到当前目录（root所有者）
COPY mtprotoproxy.py config.py ./

# 修改文件所有者并为Python解释器设置网络绑定权限
# 注意：必须在同一个RUN层中完成所有权限操作，避免层叠加导致权限失效
RUN chown tgproxy:tgproxy ./*.py && \
    setcap cap_net_bind_service=+ep /usr/bin/python3

# 切换到非root用户（增强安全性）
USER tgproxy

# 容器启动命令
CMD ["python3", "mtprotoproxy.py"]
