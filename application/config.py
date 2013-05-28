class Config(object):
    """ General configuration keys.  """
    DEBUG = False
    TESTING = False
    ASSETS_DEBUG = False


class DevelopmentConfig(Config):
    """ Configuration for development. """
    DEBUG = True
