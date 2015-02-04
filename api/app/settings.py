#!/usr/bin/env python
# -*- coding: UTF-8 -*- #

import os
from app import app

# Declare mongodb environment variables

app.config['MONGO_HOST'] = os.environ.get('MONGO_HOST')
app.config['MONGO_PORT'] = os.environ.get('MONGO_PORT')
app.config['MONGO_USERNAME'] = os.environ.get('MONGO_USERNAME')
app.config['MONGO_PASSWORD'] = os.environ.get('MONGO_PASSWORD')
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
