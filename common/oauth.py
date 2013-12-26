# coding=utf-8
""" OAuth 认证 """

from flask_oauth import OAuth

from config import DOUBAN_APP, SINA_APP


class SinaOAuth(object):
    """ 新浪 OAuth 认证参数 """

    @staticmethod
    def access_token_params(redirect_uri):
        return {
            'client_id': SINA_APP['app_key'],
            'client_secret': SINA_APP['app_secret'],
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
        }

    @classmethod
    def remote_app(cls, redirect_uri):
        """ 获取远程应用对象 """

        return OAuth().remote_app(
            'sina',
            base_url=SINA_APP['base_url'],
            request_token_url=None,
            authorize_url=SINA_APP['authorize_url'],
            access_token_url=SINA_APP['access_token_url'],
            access_token_params=cls.access_token_params(redirect_uri),
            access_token_method=SINA_APP['access_token_method'],
            consumer_key=SINA_APP['app_key'],
            consumer_secret=SINA_APP['app_secret'],
        )


class DoubanOAuth(object):
    """ 豆瓣 OAuth 认证参数 """

    @staticmethod
    def access_token_params(redirect_uri):
        return {
            'client_id': DOUBAN_APP['app_key'],
            'client_secret': DOUBAN_APP['app_secret'],
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
        }

    @classmethod
    def remote_app(cls, redirect_uri):
        """ 获取远程应用对象 """

        return OAuth().remote_app(
            'douban',
            base_url=DOUBAN_APP['base_url'],
            request_token_url=None,
            authorize_url=DOUBAN_APP['authorize_url'],
            access_token_url=DOUBAN_APP['access_token_url'],
            access_token_params=cls.access_token_params(redirect_uri),
            access_token_method=DOUBAN_APP['access_token_method'],
            consumer_key=DOUBAN_APP['app_key'],
            consumer_secret=DOUBAN_APP['app_secret'],
        )
