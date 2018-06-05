from redis import Redis


class Config():
    DEBUG = True
    SECRET_KRY = 'ABC123ASD55655'

    SESSION_TYPE = 'redis'
    redis_host = '192.168.237.129'
    SESSION_REDIS = Redis(host=redis_host, port=6379, db=12)

    # 配置数据链接
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:147159@127.0.0.1:3306/user'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 为了以后更好的扩展 兼容
