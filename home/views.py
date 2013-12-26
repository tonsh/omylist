# coding=utf-8

from flask import redirect, Response

from home import bp_home


@bp_home.route('/')
def index():
    return 'Hello World!!'


@bp_home.route('/login')
@bp_home.route('/login/<name>')
def login(name=None):
    if name == 'sina':
        return redirect('/sina/authorize')
    elif name == 'douban':
        return redirect('/douban/authorize')

    return Response('login page')
