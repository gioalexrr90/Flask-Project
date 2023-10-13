from decouple import config as env
import os

class Config():
    DEBUG = False
    TESTING = False
    
    #DB_SERVER = env['MYSQL_HOST']
    #DB_NAME = env['MYSQL_NAME']
    #DB_USER = env['MYSQL_USER']
    #DB_PASSWORD = env['MYSQL_PASSWORD']
    #DB_PORT = env['MYSQL_PORT']
    
    #@property
    #def DATABASE_URI(self):         # Note: all caps
    #    return 'mysql://{}@{}/{}'.format(self.DB_USER, self.DB_SERVER, self.DB_NAME)
    
class ProductionConfig(Config):
    #Configuracion de producción para la base de datos
    DB_SERVER = '192.168.19.32'

class DevelopmentConfig(Config):
    DB_SERVER='localhost'
    DEBUG = True
    
class TestingConfig(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    DB_SERVER = 'localhost'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'src/databases/database.db')
    
config = {
    'development': TestingConfig,
}