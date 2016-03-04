#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import argparse
import menu

import constants


class Garcon:

    def __init__(self, url, show_browser=False):
        self.url = url
        self.browser = \
            webdriver.Firefox() if show_browser else webdriver.PhantomJS()
        self.browser.get(self.url)

    def _type_input(self, id, value):
        el = self.browser.find_element_by_id(id)
        el.send_keys(value)

    def login(self, user, password, company):
        self._type_input(constants.USER_INPUT_ID, user)
        self._type_input(constants.PASS_INPUT_ID, password)
        self._type_input(constants.COMPANY_INPUT_ID, company)

        login_button = \
            self.browser.find_element_by_id(constants.LOGIN_BUTTON_ID)
        login_button.click()

    def order_the_usual(self):
        print "ordered the usual!"


def main():
    parser = \
        argparse.ArgumentParser(description='What can I get you, chubby boy?')
    parser.add_argument('--user', '-u', type=str, required=True,
                        help='your cibus user')
    parser.add_argument('--password', '-p', required=True,
                        type=str,
                        help='your cibus password')
    parser.add_argument('--company', '-c', type=str, default='gigaspaces',
                        required=False, help='your company')
    parser.add_argument('--visible', '-v', default=False,
                        required=False, help='show browser?',
                        action='store_true')
    args = parser.parse_args()

    garcon = Garcon(constants.BASE_URL, show_browser=args.visible)
    garcon.login(unicode(args.user, 'utf8'),
                 args.password,
                 args.company)

    mainMenu = menu.Menu('What can I get you, chubby boy?')
    mainMenu.indicator = '>'
    mainMenu.explicit()
    options = [{"name": "The usual!", "function": garcon.order_the_usual},
               {"name": "secondOption", "function": None},
               {"name": "thirdOption", "function": None}]
    mainMenu.addOptions(options)
    mainMenu.open()


if __name__ == '__main__':
    main()
