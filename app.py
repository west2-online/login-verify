import sys

sys.path.append('../')  # '../'表示当前目录的父目录，也即这个项目的项目目录，引入环境变量，让python认为project是一个模块，终端下也可以使用
print(sys.path)
from flask import Flask, request

app = Flask(__name__)

from flask import jsonify
from statistic.util.login_verifycode import util_login_validateCode


@app.route('/api/v1/jwch/user/validateCode', methods=['POST'])
def get_login_validateCode_v1():
    image_string = request.form.get('image')
    res = util_login_validateCode(image_string)
    return jsonify({'code': '200', 'message': 'success', 'data': str(res)}), 200


@app.route('/api/login/validateCode', methods=['POST'])
def get_login_validateCode():
    image_string = request.form.get('validateCode')
    res = util_login_validateCode(image_string)
    return jsonify({'message': str(res)}), 200


if __name__ == '__main__':
    from hypercorn.config import Config
    from hypercorn.asyncio import serve

    config = Config()
    config.bind = ["0.0.0.0:8081"]
    config.http2 = True  # 启用 HTTP/2

    import asyncio
    asyncio.run(serve(app, config))
