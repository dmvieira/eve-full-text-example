#!/usr/bin/env python
# -*- coding: utf-8 -*- #

""" Core API file. This file implements all API url
mapping and actions.
"""

import re
from bson import json_util as json
from flask import request, jsonify
from flask.ext import restful, cors
from model import hotel
from app import app

# Using Flask api resource
api = restful.Api(app)

# Enable CORS
cors = cors.CORS(app)


class Home(restful.Resource):
    """ Home resource to help users with a simple 'how to use'. """
    def get(self):
        """ This API only implement GET method. """

        return 'Please use /city or /hotel'

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

        return jsonify(result)

# Mapping url to City
api.add_resource(City, '/city')


class Hotel(restful.Resource):

    def get(self):
        """ GET from REST. Used to get hotels by city name. It's useful for
        search hotels by city. If you don't set city name it returns
        an empty json.
        :return: Hotels in json format, but mongodb is returning unicode, so I
        need to use bson utils and return as json string.
        """
        city_name = request.args.get("city_name")
        query = dict()
        result = dict()
        if city_name:
            query['city'] = city_name
            result = hotel.find(query)
        return json.dumps(dict(result=[r for r in result], ok=1.0))

# Mapping url to Hotel
api.add_resource(Hotel, '/hotel')
