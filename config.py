class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '8c84f3a20b0f6af5ef2a0a3ec6341474'


class ProductionConfig(Config):
    DEBUG = False
    FLASK_PORT = 43210


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = dict(
    dev=DevelopmentConfig,
    testing=TestingConfig,
    stage=StagingConfig,
    prod=ProductionConfig,
)
