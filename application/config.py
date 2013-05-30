import os


class Config(object):

    """ General configuration keys.  """
    DEBUG = False
    TESTING = False
    ASSETS_DEBUG = False
    TEMPLATE_FOLDER = 'templates'


class DevelopmentConfig(Config):

    """ Configuration for development. """
    DEBUG = True
