"""
@author:admin
@file: __init__.py.py
@time: 2020/07/25
"""
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')
