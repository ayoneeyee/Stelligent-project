import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG   = False 
    TESTING = False 
    SECRET_KEY = os.environ['SECRET_KEY']

    def factory(type):
        if type == 'development':
            return Development()
        if type == 'stage':
            return Stage()
        if type == 'production':
            return Production()
        assert 0, "Bad config type creation " + type
    factory = staticmethod(factory)

class Development(Config):
    DEBUG = True 
    TESTING = True 

class Stage(Config):
    DEBUG = True 

class Production(Config):
    pass

