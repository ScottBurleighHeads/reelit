import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # WTF_CSRF_ENABLED = True
    DEBUG = False
    TESTING = False
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DB_URI")

        if not value:
            raise ValueError("DB_URI is not set")

        return value

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING=True
    # WTF_CSRF_ENABLED = False
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DB_URI_TEST")

        if not value:
            raise ValueError("DB_URI_TEST is not set")

        return value

environment = os.environ.get("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()