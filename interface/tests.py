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

        # analyze root
        response = self.json_call('/', need_eval=False)

        self.assertEqual(response, 'Please use /city or /hotel')

        # verify if no other resource are visible
        response = self.app.get('/globo', content_type='application/json')

        self.assertEqual(response.status_code, 404, "Failed in status code")

if __name__ == '__main__':
    unittest.main()
