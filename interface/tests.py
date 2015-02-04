#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import unittest
from app import app


class TestInterface(unittest.TestCase):
    """ Unity tests for interface. Tests are covering all 3 resources:
    Hotel, City and Home.
    """
    def setUp(self):
        """ Setting configurations for testing. """

        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()  # running a test client

    def tearDown(self):
        """ No need for clean configurations, but stay here if needs
        someday and because is Flask default method for testing.
        """
        pass

    def test_index_get(self):
        """ Simple tests for index page.
        """

        # analyze root 2 times
        response = self.app.get('/')

        self.assertEqual(response.status_code, 200, "Failed in status code")

        response = self.app.get('/index')

        self.assertEqual(response.status_code, 200, "Failed in status code")

        # validates for vars
        response = self.app.get('/?test_var=1')

        self.assertEqual(response.status_code, 200, "Failed in status code")

        # validates for vars in index
        response = self.app.get('/index?test_var=1')

        self.assertEqual(response.status_code, 200, "Failed in status code")

        # validates for args in index
        response = self.app.get('/index/test')

        self.assertEqual(response.status_code, 404, "Failed in status code")

        # verify if no other resource are visible
        response = self.app.get('/globo', content_type='application/json')

        self.assertEqual(response.status_code, 404, "Failed in status code")

if __name__ == '__main__':
    unittest.main()
