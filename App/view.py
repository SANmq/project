"""
@author:admin
@file: view.py
@time: 2020/07/25
@description:注册蓝图
"""
from App.myFilter import app
from App.login import login
from App.rpt import rpt

app.register_blueprint(login)
app.register_blueprint(rpt)
