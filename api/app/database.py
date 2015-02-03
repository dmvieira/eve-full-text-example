import pymongo
from flask.ext.pymongo import PyMongo
from . import config
from settings import app
import time

MAXCONNECTIONS = config.getint('default', 'maxconnections')

# Wait mongodb up to connect
for i in xrange(MAXCONNECTIONS):
    try:
        mongo = PyMongo(app)
        break
    except pymongo.errors.ConnectionFailure:
        time.sleep(5)
    except:
        raise

try:
    mongo
except NameError:
    raise Exception("Try improve maxconnections and check "
                    "mongodb connection variables")