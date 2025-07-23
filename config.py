import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'devkey')
    MONGODB_SETTINGS = {
        'db': 'GestionGuias',
        'host': 'mongodb://localhost/GestionGuias'
    }
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'annevalentinaj@gmail.com'
    MAIL_PASSWORD = '34318025Alexander'
