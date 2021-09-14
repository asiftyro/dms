# config.py


class Config(object):
    """
    Common configurations
    """
    SOFTWARE_VERSION = "b1.0"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = True

    BOOTSTRAP_SERVE_LOCAL = True

    RECAPTCHA_DATA_ATTRS = {'theme': 'white'}  # 'red' | 'white' | 'blackglass' | 'clean' | 'custom'

    EXECUTOR_TYPE = "thread"  # or, process
    EXECUTOR_MAX_WORKERS = 5


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    SQLALCHEMY_ECHO = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
