"""
@author:admin
@file: __init__.py.py
@time: 2020/07/26
"""
from flask import Blueprint, render_template, make_response, request
from App.dbModel import User, db
from time import time

login = Blueprint('login', __name__)


@login.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        if request.cookies.get('user'):
            username = request.cookies.get('user').split('&')[0]
            last = request.cookies.get('user').split('&')[1]
            user = User.query.filter(User.name == username, User.last == last)
            if user:
                return render_template('rptHome.html')
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')
    else:
        username = request.form.get('user')
        password = request.form.get('password')
        if username and password:
            user = User.query.filter(User.name == username, User.password == password).first()
            if user:
                user.last = int(time())
                cookies = '{}&{}'.format(username, int(user.last))
                resp = make_response(render_template('rptHome.html'), 200)
                resp.set_cookie('user', cookies)
                db.session.commit()
                return resp
            else:
                return render_template('login.html', login='密码错误')
        else:
            return render_template('login.html', login='请输入用户名')
