class CommonConfig(object):
    TOKEN_VALIDITY = 60 * 60 * 24
    EXCLUDE_URL = [
        '/api/account/login',
        '/api/account/register',

    ]


class DebugMode(CommonConfig):
    DEBUG=True
    SECRET_KEY='SGHJK34H5JKP5OJO6J@#$%^&'
    SESSION_COOKIE_NAME='NOT SESSION'

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/cloud_note'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    PORT = 5000


class TestingMode(CommonConfig):
    TESTING=True
    SECRET_KEY='#$%^&*(*&^%$%^&*(*&^&*()_)(*SGHJK34H5JKP5OJO6J@#$%^&'
    SESSION_COOKIE_NAME='MD5_DATA'

class ProductionMode(CommonConfig):
    DEBUG=False
    TESTING=False