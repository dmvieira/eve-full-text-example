#!/usr/bin/env python

""" This file enable database populate using HU scrapper.
Here it connects to HU website and import some items to
mongodb database.
"""

from beautifulscraper import BeautifulScraper
import pymongo
import os
import time
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read(os.path.join(os.environ['ROOT_DIR'], 'populate', 'populate.cfg'))

scraper = BeautifulScraper()

# Setting constants from config file and environment
HOTEL_FIELDS = config.options('hotel_fields')
MAXCONNECTIONS = config.getint('default', 'maxconnections')
MAXPAGES = config.getint('default', 'maxpages') + 1
MONGO_HOST = os.environ['MONGO_HOST']
MONGO_PORT = os.environ['MONGO_PORT']
MONGO_DBNAME = os.environ['MONGO_DBNAME']
MONGO_USERNAME = os.environ['MONGO_USERNAME']
MONGO_PASSWORD = os.environ['MONGO_PASSWORD']

# Wait mongodb up to connect
for i in xrange(MAXCONNECTIONS):
    try:
        client = pymongo.MongoClient(MONGO_HOST, int(MONGO_PORT))
        break
    except pymongo.errors.ConnectionFailure:
        time.sleep(5)
    except:
        raise

try:
    client
except NameError:
    raise Exception("Try improve maxconnections and check "
                    "mongodb connection variables")

# Connect to mongodb and remove all data from hotel (if exists)
db = client[MONGO_DBNAME]
db.add_user(MONGO_USERNAME, MONGO_PASSWORD)
db.hotel.remove()


def reset_fields(fields):
    """ Reset all fields to ensure that new fields will be added in next
    lines.
    """
    fields = dict()
    for field in config.options('all_fields'):
        fields[field] = None

    return fields


fields = dict()

# Do scrapping
for num in xrange(1, MAXPAGES):
    url = 'http://www.hotelurbano.com/hoteis/x/%s' % num
    body = scraper.go(url)
    city = body.select('.marinho strong')
    if len(city) == 4:
        fields['city'] = city[1].text
    hotels = body.select('.box-nome-hoteis p')
    for key, hotel in enumerate(hotels):
        index = key % len(HOTEL_FIELDS)
        fields[HOTEL_FIELDS[index]] = hotel.string
        if index == len(HOTEL_FIELDS) - 1:
            db.hotel.insert(fields)
            del fields['_id'] # removing id added to fields by mongodb

    fields = reset_fields(fields)
