#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import unittest
from bson import json_util as json
from app import app


class TestApi(unittest.TestCase):
    """ Unity tests for api. Tests are covering all 3 resources:
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

    def json_call(self, url, need_eval=False):
        """ Make all json calls for all testing functions. Make json request,
        read data from json and verify status code for all requests.
        :param url: url for json call.
        :param need_eval: if json call needs eval or not. Hotel needs
        eval because it is using json as string (mongodb problems).
        :return: json data for further tests.
        """

        response = self.app.get(url, content_type='application/json')

        # validates status code
        self.assertEqual(response.status_code, 200, "Failed in status code")
        # json data received
        data = json.loads(response.data)

        if need_eval:
            return eval(data)
        else:
            return data

    def test_home_get_call(self):
        """ Simple tests for home API and if just city and hotel are really
        accessible.
        """

        # analyze root
        response = self.json_call('/', need_eval=False)

        self.assertEqual(response, 'Please use /city or /hotel')

        # verify if no other resource are visible
        response = self.app.get('/globo', content_type='application/json')

        self.assertEqual(response.status_code, 404, "Failed in status code")

        # validates for vars
        response = self.app.get('/?test_var=1')

        self.assertEqual(response.status_code, 200, "Failed in status code")

    def test_hotel_get_call(self):
        """ Hotel API tests. If return nothing then we get an dict with ok
        and empty result. """

        # validates if /hotel works returning nothing
        response = self.json_call('/hotel', need_eval=True)

        self.assertEqual(response, dict(ok=1.0,
                                        result=[]))

        # validates if correct usage is working
        # I know my dataset, if not I should get database and
        # first city name for testing. By now I know that Arenal is
        # safe to use.
        response = self.json_call('/hotel?city_name=Arenal', need_eval=True)

        self.assertGreater(len(response['result']), 1)

        # validates if var null is working
        response = self.json_call('/hotel?city_name=', need_eval=True)

        self.assertEqual(response, dict(ok=1.0,
                                        result=[]))

        # validates if is not accepting other var
        response = self.json_call('/hotel?name=Arenal', need_eval=True)

        self.assertEqual(response, dict(ok=1.0,
                                        result=[]))

        # validates for other var null
        response = self.json_call('/hotel?name=', need_eval=True)

        self.assertEqual(response, dict(ok=1.0,
                                        result=[]))

        # validates for args in hotel
        response = self.app.get('/hotel/test')

        self.assertEqual(response.status_code, 404, "Failed in status code")

    def test_city_get_call(self):
        """ City API tests. If return nothing then we get an dict with ok
        and empty result.
        """

        # validates if city is working and returning nothing
        response = self.json_call('/city', need_eval=False)

        self.assertEqual(response, dict(ok=1.0,
                                        result=[]))

        # testing if normal call is working, but I only used Arenal because
        # I know my database will not change. Better approach should be
        # using a random database record for test.
        response = self.json_call('/city?name=Arenal', need_eval=False)

        self.assertEqual(len(response['result']), 1)

        # testing with lowercase. It should work in any case.
        response = self.json_call('/city?name=arenal', need_eval=False)

        self.assertEqual(len(response['result']), 1)

        # testing with uppercase. It should work in any case.
        response = self.json_call('/city?name=ARENAL', need_eval=False)

        self.assertEqual(len(response['result']), 1)

        # testing with 'randomcase'. It should work in any case.
        response = self.json_call('/city?name=ArEnAl', need_eval=False)

        self.assertEqual(len(response['result']), 1)

        # testing only with part of the word. Should work as autocomplete.
        # Again, I know that exists more than one item starting with 'a' in
        # my database, but correct approach should be searching in database
        # for a test case.
        response = self.json_call('/city?name=a', need_eval=False)

        self.assertGreater(len(response['result']), 1)

        # testing with var null
        response = self.json_call('/city?name=', need_eval=False)

        self.assertEqual(response, dict(ok=1.0,
                                        result=[]))

        # testing another var. Should return nothing
        response = self.json_call('/city?city=Arenal', need_eval=False)

        self.assertEqual(response, dict(ok=1.0,
                                        result=[]))

        # testing with another var null
        response = self.json_call('/city?city=', need_eval=False)

        self.assertEqual(response, dict(ok=1.0,
                                        result=[]))

        # validates for args in city
        response = self.app.get('/city/test')

        self.assertEqual(response.status_code, 404, "Failed in status code")

if __name__ == '__main__':
    unittest.main()
