import os


class Config:
    file_path = os.path.abspath(os.getcwd()) + "\site.db"
    SECRET_KEY = '6f5bf1088a10983594947efe6fc5305f0e066b75450fbfa93158af364fc849e3'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + file_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
