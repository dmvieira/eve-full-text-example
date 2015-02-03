#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import json
from bson import json_util
from flask.ext import restful
from database import mongo
from app import app

api = restful.Api(app)

class Home(restful.Resource):
    def get(self):
        return json.dumps(['Please use /city or /hotel'])
api.add_resource(Home, '/')

class City(restful.Resource):
    def get(self):
        query = mongo.db.hotel.aggregate([{'$group': {'_id': "$city"}}])
        return json.dumps(query, default=json_util.default)

api.add_resource(City, '/city')

class Hotel(restful.Resource):
    def get(self, city_name):
        query = mongo.db.hotel.find({'city': city_name})
        return json.dumps([item for item in query], default=json_util.default)

api.add_resource(Hotel, '/hotel/<string:city_name>')