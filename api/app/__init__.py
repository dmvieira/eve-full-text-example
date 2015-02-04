#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import ConfigParser
import os
from flask import Flask


app = Flask(__name__)


# Get configuration file
config = ConfigParser.RawConfigParser()
config.read(os.path.join(os.environ['ROOT_DIR'], 'api', 'api.cfg'))

from app import core
