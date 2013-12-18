# coding=utf-8
""" Server start """

from flask import Flask

import env
from home import bp_home
from user import bp_user


app = Flask(__name__)

# configuration
if env.ENV == 'production':
    app.config.from_object('config.ProductionConfig')
elif env.ENV == 'testing':
    app.config.from_object('config.TestingConfig')
elif env.ENV == 'development':
    app.config.from_object('config.DevelopmentConfig')

# regist blueprint
app.register_blueprint(bp_home)
app.register_blueprint(bp_user, url_prefix='/user')

app.run(
    host=env.APP_HOST,
    port=env.APP_PORT,
)
