#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    city_url = 'http://localhost:%s/city' % os.environ.get('API_PORT')
    hotel_url = 'http://localhost:%s/hotel' % os.environ.get('API_PORT')
    return render_template('index.html',
                           city_url=city_url,
                           hotel_url=hotel_url)
