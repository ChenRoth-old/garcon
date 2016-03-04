#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from garcon import Garcon

class TestGarcon(unittest.TestCase):

    def test_login(self):
        garcon = Garcon('http://cibus.co.il')
        credentials = {
            'user': 'redacted',
            'password': 'redacted',
            'company': 'gigaspaces'
        }
        garcon.login(**credentials)
        token = garcon.browser.get_cookie('token')
        self.assertIsNotNone(token, 'login failed')

if __name__ == '__main__':
    unittest.main()