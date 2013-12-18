# coding=utf-8
""" The config options!

    Diffrent environment have diffrent configurations.
"""

import env


class Config(object):
    """ The default configuration. """

    # Default disabled debug mode.
    # Recommend enabled in development environment.
    DEBUG = False

    # Default disabled testing mode.
    # Recommend enabled in testing environment.
    TESTING = False

    # Application stored directory.
    APP_DIR = env.APP_DIR

    # Application host
    APP_HOST = '0.0.0.0'
    APP_PORT = 5000


class ProductionConfig(Config):
    """ Production environment configuration. """
    pass


class TestingConfig(Config):
    """ Testing environment configuration.
        It will Cover the default Config.
    """

    TESTING = True


class DevelopmentConfig(Config):
    """ Development environment configuration.
        It will Cover the default Config.
    """

    DEBUG = True


app_config = None
if env.ENV == 'production':
    app_config = ProductionConfig
elif env.ENV == 'testing':
    app_config = TestingConfig
elif env.ENV == 'development':
    app_config = DevelopmentConfig
