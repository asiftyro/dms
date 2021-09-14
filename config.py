# config.py


class Config(object):
    """
    Common configurations
    """
    SOFTWARE_VERSION = "b1.0"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_SERVE_LOCAL = True
    WTF_CSRF_ENABLED = True
    RECAPTCHA_DATA_ATTRS = {'theme': 'white'}  # 'red' | 'white' | 'blackglass' | 'clean' | 'custom'


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
