from redis import StrictRedis
class Config:

    DEBUG=True

    SECRET_KEY = 'dxdvvrEG3IvY8kz1FyE7rYOZexjl+IsiSD8EBo8J7iEMwQ4pLuY8pg=='

    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/info_python37'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE= 'redis'

    SESSION_REDIS= StrictRedis(host='127.0.0.1', port=6379)

    SESSION_USE_SIGNER= True

    PERMANENT_SESSION_LIFETIME= 86400


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

config_dict={
    'development':DevelopmentConfig,
    'production':ProductionConfig
}