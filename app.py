#! /usr/bin/env python
# -*- coding:utf-8 -*-
#flask框架 需要提前装一下 pip install flask
import logging
logging.basicConfig(level=logging.INFO, format='127.0.0.1 - - [%(asctime)s - %(name)s - %(levelname)s - %(message)s]')
logger = logging.getLogger(__name__)
from flask import Flask, request, render_template
import json
import util
import db
app = Flask(__name__) #首先定义一个应用程序
# 路由配置
# @app.route('/')
# # 定义处理函数
# def test():
#     #处理逻辑
#     # List = [1,2,3,4,5]
#     return 'hello,world!'     #响应
#     # return render_template('test.html',Lst = List), 200

@app.route('/', methods=['GET'])
#定义处理函数
def form():
      # 引入模板
    return render_template('index.html'), 200

@app.route('/signup', methods=['GET', 'POST'])
def enroll():
    if request.method == 'GET':
        return render_template('enroll.html'), 200
    else:
        #接受数据
        username = request.form.get('form-username', default='user')
        password = request.form.get('form-password', default='pass')
        logger.info("注册的用户是："+str(username))
        logger.info("用户的密码是："+str(password))
        if db.get_pass(username):
            return 'existed'
        else:
            db.save_user(username, password)
            return 'ok'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html'), 200
    else:
        username = request.form.get('form-username', default='user')
        password = request.form.get('form-password', default='pass')
        logger.info("登录的用户是："+str((username)))
        logger.info("用户的密码是："+str(password))
        db_pass = db.get_pass(username)
        if not db_pass:
            return 'none'
        elif db_pass != password:
            return 'wrong'
        else:
            return 'right'

@app.route('/user', methods=['POST'])
def login_success():
    username = request.form.get('username', default='user')
    return render_template('user.html', username=username), 200

if __name__ == '__main__':
    host = util.get_config()["host"]
    port = int(util.get_config()["port"])
    debug = util.get_config()["debug"]
    if debug == "True":
        debug = True
    else:
        debug = False
    print(debug)
    app.run(host=host, port=port, threaded=True, debug=debug)
