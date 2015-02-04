#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import unittest
from bson import json_util as json
from app import app


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_hotel_get_call(self):
        response = self.app.get('/hotel', content_type='application/json')

        self.assertEqual(json.loads(response.data), ["ok", "result"])


if __name__ == '__main__':
    unittest.main()
