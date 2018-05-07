import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    APP_NAME = "AutoHomeGrade"
    UPLOAD_FOLDER = 'uploads/'
    SECRET_KEY = os.environ.get("SECRET_KEY") or "asdjfklj23k409UULKJKL#J$jkljflkajsdf"


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "prod.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    "dev": DevConfig,
    "prod": ProdConfig,
    "default": DevConfig
}
