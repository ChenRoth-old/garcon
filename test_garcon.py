#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from garcon import Garcon


class TestGarcon(unittest.TestCase):

    def setUp(self):
        self.garcon = Garcon('http://cibus.co.il', show_browser=True)
        self.credentials = {
            'user': 'redacted',
            'password': 'redacted',
            'company': 'gigaspaces'
        }

    def _test_login(self):
        self.garcon.login(**self.credentials)
        token = self.garcon.browser.get_cookie('token')
        self.assertIsNotNone(token, 'login failed')

    def test_the_usual(self):
        self.garcon.login(**self.credentials)
        self.garcon.order_the_usual()

if __name__ == '__main__':
    unittest.main()
