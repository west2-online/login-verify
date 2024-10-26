# 设置基础镜像
FROM python:3.9-slim AS builder
# 设置代码文件夹工作目录
WORKDIR /statistic
# 复制当前代码文件到容器中
ADD . /statistic
# 设置时间
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# 安装所需的包，这里的requirements文件名需和项目生成的一致
RUN pip install --no-cache-dir gunicorn gevent
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir opencv-python-headless
#构建运行镜像
FROM python:3.9-slim
#设置代码文件夹工作目录
WORKDIR /statistic  
#复制构建好的包
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /statistic /statistic
#暴露8081端口
EXPOSE 8081
# 执行入口文件
CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app", "--preload"]