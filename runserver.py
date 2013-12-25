# coding=utf-8
""" Server start """

from flask import Flask

import env
from home import bp_home
from user import bp_user


app = Flask(__name__)

# configuration
if settings.ENV == 'production':
    app.config.from_object('app_config.ProductionConfig')
elif settings.ENV == 'testing':
    app.config.from_object('app_config.TestingConfig')
elif settings.ENV == 'development':
    app.config.from_object('app_config.DevelopmentConfig')

# regist blueprint
app.register_blueprint(bp_home)
app.register_blueprint(bp_user, url_prefix='/user')

app.run(
    host=env.APP_HOST,
    port=env.APP_PORT,
)
