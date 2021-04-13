class BaseConfig(object):
    SECRET_KEY = ""
#    DEBUG = True
    DB_NAME = "sales_cards"
    DB_USER = "admin"
    DB_PASS = "admin"
    DB_SERVICE = "localhost"
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )
