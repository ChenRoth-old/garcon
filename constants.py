
BASE_URL = 'http://cibus.co.il'

LOGIN_FORM_PREFIX = 'ctl00_LoginForm1_'

USER_INPUT_ID = '{}txtUserName'.format(LOGIN_FORM_PREFIX)
PASS_INPUT_ID = '{}txtPassword'.format(LOGIN_FORM_PREFIX)
COMPANY_INPUT_ID = '{}txtCompany'.format(LOGIN_FORM_PREFIX)
LOGIN_BUTTON_ID = '{}btnLogin'.format(LOGIN_FORM_PREFIX)
PREV_ORDERS_ID = 'ctl00_HolderBody_Rest1_prevOrders'
FIRST_PREV_ORDER_ID = 'ctl00_HolderBody_Rest1_dtlPrev_ctl00_btnOrder'
SAVE_ORDER_ID = 'ctl00_HolderBody_btnSaveOrder'
PHANTOMJS_PATH = 'node_modules/phantomjs/bin/phantomjs'
