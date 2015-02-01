#!/usr/bin/env python

"""
This file enable database populate using HU scrapper.
Here it connects to HU website and import some items to
mongodb database.
"""

from beautifulscraper import BeautifulScraper
import pymongo
import os
import time
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read(os.path.join(os.environ['ROOT_DIR'], 'config', 'populate.cfg'))

scraper = BeautifulScraper()

# setting constants
HOTEL_FIELDS = config.options('hotel_fields')
MAXCONNECTIONS = config.getint('default', 'maxconnections')
MAXPAGES = config.getint('default', 'maxpages') + 1
MONGO_HOST = os.environ['MONGO_HOST']
MONGO_PORT = os.environ['MONGO_PORT']
MONGO_DBNAME = os.environ['MONGO_DBNAME']
MONGO_USERNAME = os.environ['MONGO_USERNAME']
MONGO_PASSWORD = os.environ['MONGO_PASSWORD']

for i in xrange(MAXCONNECTIONS):
    try:
        client = pymongo.MongoClient(MONGO_HOST, int(MONGO_PORT))
        break
    except pymongo.errors.ConnectionFailure:
        time.sleep(5)
    else:
        raise

db = client[MONGO_DBNAME]
db.add_user(MONGO_USERNAME, MONGO_PASSWORD)
db.hotel.remove()


def reset_fields(fields):
    """ Re """
    fields = dict()
    for field in config.options('all_fields'):
        fields[field] = None

    return fields


fields = dict()

for num in xrange(1, MAXPAGES):
    url = 'http://www.hotelurbano.com/hoteis/x/%s' % num
    body = scraper.go(url)
    city = body.select('.marinho strong')
    if len(city) == 4:
        fields['city'] = city[1].text
    hotels = body.select('.box-nome-hoteis p')
    for key, hotel in enumerate(hotels):
        index = key % 3
        fields[HOTEL_FIELDS[index]] = hotel.string
        if index == 2:
            db.hotel.insert(fields)
            del fields['_id']

    fields = reset_fields(fields)
