import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("mysql://user:user123@db:3306/flask_api")
    SQLALCHEMY_TRACK_MODIFICATIONS = False