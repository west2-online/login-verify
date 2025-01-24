# 第一阶段：构建 Python 应用
FROM python:3.9-slim AS builder

# 设置工作目录
WORKDIR /statistic

# 复制当前代码文件到容器中
COPY . /statistic

# 设置时区
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# 安装所需的包
RUN pip install --no-cache-dir hypercorn
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir opencv-python-headless

# 第二阶段：构建运行镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /statistic

# 从构建阶段复制 Python 环境
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /statistic /statistic

# 暴露端口
EXPOSE 8081

# 启动命令：使用 Hypercorn 运行 Flask 应用
CMD ["hypercorn", "app:app", "--bind", "0.0.0.0:8081"]