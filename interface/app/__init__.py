#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from flask import Flask
from flask_bootstrap import Bootstrap
from flaskext.scss import Scss


app = Flask(__name__)
from app import views  # To avoid circular imports

# Adding bootstrap to Flask
Bootstrap(app)

# Adding jinja support to jade
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

# Adding Flask support for scss
Scss(app)
