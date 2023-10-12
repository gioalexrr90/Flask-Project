from src import app
from flask_pymongo import PyMongo
from decouple import config

_HOST = config['MONGODB_HOST']
_PORT = config['MONGODB_PORT']
_DB_NAME = config['MONGODB_NAME']
_USER = config['MONGODB_USER']
_PASSWORD = config['MONGODB_PASSWORD']

app.config["MONGO_URI"] = "mongodb://{}:{}/{}".format(_HOST, _PORT, _DB_NAME)

mongo = PyMongo(app)
