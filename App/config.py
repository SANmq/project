"""
@author:admin
@file: config.py.py
@time: 2020/07/25
@description:基本配置，数据库配置等
"""

from datetime import timedelta

DEBUG = True
SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
HOST = "192.168.0.134"
PORT = 8686

# app.jinja_env.trim_blocks = True  #  去掉空格
# app.jinja_env.lstrip_blocks = True

# 数据库设置
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:2221@192.168.0.230:3306/edw'  # 默认数据库
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_BINDS = {
    'da': 'mysql+mysqlconnector://root:2221@192.168.0.230:3306/da',  # 另外配置的数据库
    'test': 'mysql+mysqlconnector://root:2221@192.168.0.230:3306/test',
}
