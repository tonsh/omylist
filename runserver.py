# coding=utf-8
""" Server start """

import env
#from config import app_config
from user import app

if env.ENV == 'production':
    app.config.from_object('config.ProductionConfig')
elif env.ENV == 'testing':
    app.config.from_object('config.TestingConfig')
elif env.ENV == 'development':
    app.config.from_object('config.DevelopmentConfig')

app.run(
    host=env.APP_HOST,
    port=env.APP_PORT,
)
