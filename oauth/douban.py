# coding=utf-8
""" 基于豆瓣的应用访问 """

from flask import url_for, Response

from common.oauth import DoubanOAuth
from config import APP_BASE_URL
from oauth import bp_douban


redirect_uri = APP_BASE_URL + '/douban/token'
douban = DoubanOAuth.remote_app(redirect_uri)


@bp_douban.route('/')
def index():
    return 'Hello douban!'


@bp_douban.route('/authorize')
def auth():
    callback = APP_BASE_URL + url_for('.get_token')
    return douban.authorize(callback=callback)


@bp_douban.route('/token')
@douban.authorized_handler
def get_token(resp):
    return Response(resp)
