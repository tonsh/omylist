# coding=utf-8
""" Server start """

from flask import Flask

import config
from home import bp_home
from user import bp_user


app = Flask(__name__)

# configuration
if config.ENV == 'production':
    app.config.from_object('app_config.ProductionConfig')
elif config.ENV == 'testing':
    app.config.from_object('app_config.TestingConfig')
elif config.ENV == 'development':
    app.config.from_object('app_config.DevelopmentConfig')

# regist blueprint
app.register_blueprint(bp_home)
app.register_blueprint(bp_user, url_prefix='/user')

app.run(
    host=config.APP_HOST,
    port=config.APP_PORT,
)
