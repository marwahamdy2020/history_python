import os


class Config:
 #    basce configrations
    DEBUG = False
    PORT = os.environ.get('PORT') or 5000
    ENV = os.environ.get('ENV')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class development(Config):
    #     development configrations
    DEBUG = True


class production(Config):
    #     production configrations
    PORT = os.environ.get('PORT') or 8080
