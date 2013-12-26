# coding=utf-8

from flask import redirect, request, Response

from home import bp_home


@bp_home.route('/')
def index():
    return 'Hello World!!'


@bp_home.route('/login')
def login():
    t = request.args.get('type')
    if t == 'sina':
        return redirect('/sina/authorize')
    elif t == 'douban':
        return redirect('/douban/authorize')
    return Response('login page')
