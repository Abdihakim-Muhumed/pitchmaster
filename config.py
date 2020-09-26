import os 
class Config :
    '''General config parent class'''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ABDIHAKIM:CIT0017@localhost/pitchmaster'
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
