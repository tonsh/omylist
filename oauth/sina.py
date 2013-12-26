# coding=utf-8
""" 基于新浪的应用访问 """

from flask import url_for, Response

from common.oauth import SinaOAuth
from config import APP_BASE_URL
from oauth import bp_sina


redirect_uri = APP_BASE_URL + '/sina/token'
sina = SinaOAuth.remote_app(redirect_uri)


@bp_sina.route('/')
def index():
    return 'Hello sina!'


@bp_sina.route('/authorize')
def auth():
    callback = APP_BASE_URL + url_for('.get_token')
    return sina.authorize(callback=callback)


@bp_sina.route('/token')
@sina.authorized_handler
def get_token(resp):
    import json

    resp = json.loads(resp.keys()[0])
    return Response(resp)
