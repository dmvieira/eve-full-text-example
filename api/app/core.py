#!/usr/bin/env python
# -*- coding: utf-8 -*- #

""" Core API file. This file implements all API url
mapping and actions.
"""

import json
import re
from bson import json_util
from flask import request
from flask.ext import restful
from flask.ext.cors import CORS
from model import hotel
from app import app

# Using Flask api resource
api = restful.Api(app)

# Enable CORS
cors = CORS(app)

class Home(restful.Resource):
    """ Home resource to help users with a simple 'how to use'. """
    def get(self):
        """ This API only implement GET method. """

        return json.dumps(['Please use /city or /hotel'])

# Mapping url to Home
api.add_resource(Home, '/')


class City(restful.Resource):
    """ City resource to manage cities in database as serve as API. """

    def get(self):
        """ GET from REST. Used to get cities by name. It's useful for
        autocomplete applications. If you don't set city name it returns
        an empty json.
        :return: Cities in json format.
        """
        name = request.args.get("name")
        result = dict(ok=1.0, result=[])
        if name:
            aggregate = [
                {'$match': {'city': {'$regex': re.compile("^%s" % name,
                                                          re.IGNORECASE)}}},
                {'$group': {'_id': "$city"}}
            ]
            result = hotel.aggregate(aggregate)

        return json.dumps(result['result'], default=json_util.default)

# Mapping url to City
api.add_resource(City, '/city')


class Hotel(restful.Resource):

    def get(self):
        """ GET from REST. Used to get hotels by city name. It's useful for
        search hotels by city. If you don't set city name it returns
        an empty json.
        :return: Hotels in json format.
        """
        city_name = request.args.get("city_name")
        query = dict()
        result = dict(ok=1.0, result=[])
        if city_name:
            query['city'] = city_name
            result = hotel.find(query)
        return json.dumps([item for item in result], default=json_util.default)

# Mapping url to Hotel
api.add_resource(Hotel, '/hotel')