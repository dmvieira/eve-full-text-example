#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Runs api using settings configuration from other files.

import os
from app import app


if __name__ == '__main__':
    app.run(debug=True,
            port=int(os.environ.get('API_PORT')))
