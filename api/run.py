#!/usr/bin/env python

# Runs api using settings configuration and database schema from other files.

from eve import Eve
app = Eve()

if __name__ == '__main__':
    app.run()
