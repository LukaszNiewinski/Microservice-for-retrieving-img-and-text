import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_DATABASE_URI = "postgresql://hello_semantive:hire_me@db:5432/retrieve_data_dev"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
