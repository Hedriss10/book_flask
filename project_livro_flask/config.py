"""
    Config.py é responsável para avisa para o Python em que ambiente nosso
    proejeto está rodand, se estará em produção, teste, ou desenvolvimento     
"""

import os 
import random, string


class Config(object):
    CSRF_ENABLED = True 
    SECRET = 'ysb_92=qe#djf8%ng+a*#4rt#5%3*4k5%i2bck*gn@w3@f&-&'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))    
    APP = None



class DevelopementCofing(Config):
    TESTING = True 
    DEBUG = True 
    IP_HOST = 'locahost'
    PORT_HOST = 8000
    URL_MAIN =  'http://%s:%s/' % (IP_HOST, PORT_HOST)
    
    
class TestingConfig(Config):
    TESTING = True 
    DEBUG = True 
    IP_HOST = 'locahost' # geralmente é um ip do servidor na nuvem e não no endereço da máquina local
    PORT_HOST = 8000
    URL_MAIN =  'http://%s:%s/' % (IP_HOST, PORT_HOST)
    
    
    
class ProductionConfig(Config):
    TESTING = True 
    DEBUG = True 
    IP_HOST = 'locahost' # geralmente é um ip do servidor na nuvem e não no endereço da máquina local
    PORT_HOST = 8000
    URL_MAIN =  'http://%s:%s/' % (IP_HOST, PORT_HOST)
    
    
    
app_config =  {
    'development' : DevelopementCofing(),
    'testing' : TestingConfig(),
    'production': ProductionConfig()
}


app_active = os.getenv("FLASK_ENV")