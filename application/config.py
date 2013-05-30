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
    DB_URL = 'sqlite:///' + os.path.join(
        os.path.abspath(__package__), 'dev.db')
