__author__ = 'alandinneen'
from json import dumps

class Configuration(object):
    MONGO_IP = 'localhost'
    MONGO_PORT = 27017
    MONGO_DB = 'uploads'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_APP_NAME = 'dt_regression_api'
    MAIL_SERVER = 'smtp.email.com'
    MAIL_PORT = 587
    MAIL_DEFAULT_SENDER = 'sender@email.com'
    MAIL_USER = 'useraccount@email.com'
    MAIL_USER_PASS = 'useraccountpassword@email.com'
    MAIL_RECIPIENT = 'recipient@email.com'
    RSSWEBSITES = 'rssWebSites.txt'




    # Application specific cofiguration methods.



class DevConfiguration(Configuration):
    DEBUG = True
    host = "127.0.0.1"
    port = 8001

