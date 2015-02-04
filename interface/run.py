#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
from app import app

# Starts interface

if __name__ == '__main__':
    app.run(debug=os.environ.get('DEVELOP_ENV', True),
            port=int(os.environ.get('INTERFACE_PORT')))
