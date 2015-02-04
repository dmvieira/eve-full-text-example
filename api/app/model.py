#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import pymongo
from flask.ext.pymongo import PyMongo
from . import config
from settings import app
import time


class BaseModel(object):
    """ Base model for mongodb collections. This is the structure to
    continue other models.
    """
    def __init__(self, database):
        """ Receive database, declare context and set collection and
        structure as None to be defined in other classes.
        :param database: Receive mongodb instance connected to database
        """
        self.__context = app.app_context()
        self.__collection = None
        self.structure = None
        self.database = database

    @property
    def collection(self):
        """ Getter for collection that raise an error if collection is
        not defined, because it's probably not using inheritance.
        """
        if not self.__collection:
            raise NotImplementedError

        return self.__collection

    @collection.setter
    def collection(self, value):
        """ Setter for collection. """
        with self.__context:
            self.__collection = self.database.db[value]

class HotelModel(BaseModel):
    """ Defines hotel model for mongodb. """
    def __init__(self, database):
        """ Define structure and collection name for this model in mongodb.
        Collection is used to declare model as variable below.
        :param database: receives database and passes to BaseModel
        :return:
        """
        super(HotelModel, self).__init__(database)
        self.structure = {
            'name': str,
            'city': str,
            'phone': str,
            'location': str,
        }
        self.collection = 'hotel'


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

# Define Models as variables to simplify usage

hotel = HotelModel(mongo).collection