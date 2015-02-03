#!/usr/bin/env python

import os
from app import app

app.run(debug=True,
        port=int(os.environ.get('INTERFACE_PORT')))
