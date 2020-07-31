"""
@date:2020-07-27
@time：13:43
@author:smq
@description:描述
"""
from App.dbModel import User


def prove_login(cookie):
    if cookie and '&' in cookie:
        username = cookie.split('&')[0]
        last = cookie.split('&')[1]
        user = User.query.filter(User.name == username, User.last == last).first()
        return True if user else False
    else:
        return False


def get_user_config(cookie):
    if cookie and '&' in cookie:
        username = cookie.split('&')[0]
        last = cookie.split('&')[1]
        user = User.query.filter(User.name == username, User.last == last).first()
        return user
    else:
        return {}
