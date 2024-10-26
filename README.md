
本项目用于获取教务处的验证码的解析结果 (2024 10.26) 备份

本项目默认使用8081端口
提示：如果需要修改端口，有三处地方需要修改
1. app.py 的 app.run
2. gunicorn 的 bind
3. dockerfile 的expose

注：docker 的 net=host 模式似乎不可用