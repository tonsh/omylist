# coding=utf-8
""" user views """

from user import bp_user


@bp_user.route('/')
def index():
    return 'Hello World!'
