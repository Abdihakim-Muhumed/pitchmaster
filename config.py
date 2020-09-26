import os 
class Config :
    '''General config parent class'''
    SECRET_KEY="powerful secretkey"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ABDIHAKIM:12345678@localhost/pitchmaster'
class ProdConfig(Config): 
    '''productio config  child class
        arg: 
            config: parent config class

        '''
    pass

class DevConfig(Config):
    '''Development configuration child class
    arg:
        Config: parent configurations class
        '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
