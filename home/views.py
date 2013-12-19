# coding=utf-8

from home import bp_home


@bp_home.route('/')
def index():
    return 'Hello World!!'
