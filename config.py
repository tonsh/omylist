# coding=utf-8
""" 配置文件 """

from env_config import *

SINA_APP = {
    'base_url': 'https://api.weibo.com/oauth2',
    'authorize_url': 'https://api.weibo.com/oauth2/authorize',
    'access_token_url': 'https://api.weibo.com/oauth2/access_token',
    'access_token_method': 'POST',
    'app_key': SINA_APP_KEY,
    'app_secret': SINA_APP_SECRET,
}

DOUBAN_APP = {
    'base_url': 'https://api.douban.com/v2',
    'authorize_url': 'https://www.douban.com/service/auth2/auth?'
                     'response_type=code',
    'access_token_url': 'https://www.douban.com/service/auth2/token',
    'access_token_method': 'POST',
    'app_key': DOUBAN_APP_KEY,
    'app_secret': DOUBAN_APP_SECRET,
}
