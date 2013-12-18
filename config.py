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
