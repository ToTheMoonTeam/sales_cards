import os

class BaseConfig(object):
    SECRET_KEY = ""
#    DEBUG = True
    DB_NAME = os.environ.get('DN_NAME') or "sales_cards"
    DB_USER = os.environ.get('DB_USER') or "postgres"
    DB_PASS = os.environ.get('DB_PASS') or "postgres"
    DB_SERVICE = os.environ.get('DB_SERVICE') or "localhost"
    DB_PORT = os.environ.get('DB_PORT') or  5432
    SQLALCHEMY_DATABASE_URI ='postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )
