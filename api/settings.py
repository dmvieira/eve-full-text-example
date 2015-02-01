#!/usr/bin/env python

import os
from database import schema

RESOURCE_METHODS = ['GET']

ITEM_METHODS = ['GET']

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')

hotel = {
    'item_title': 'hotel',

    'additional_lookup': {
                'url': 'regex("[\w]+")',
                'field': 'city'
            },

    'cache_control': 'max-age=5000,must-revalidate',
    'cache_expires': 5000,

    'schema': schema
}

DOMAIN = {
    'hotel': hotel,
}
