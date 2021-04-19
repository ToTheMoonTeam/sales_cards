class BaseConfig(object):
    SECRET_KEY = ""
#    DEBUG = True
    DB_NAME = "sales_cards"
    DB_USER = "admin"
    DB_PASS = "admin"
    DB_SERVICE = "sales_cards"
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = "postgres://tlztsbmuwbwchz:6f2409c20ffb3143636b544fc9cfc5a415aed459cd52d293684f3359f84bb350@ec2-107-20-153-39.compute-1.amazonaws.com:5432/d1962096amtmnu"
