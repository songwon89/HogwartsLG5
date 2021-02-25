#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_wechat.page.base_page import BasePage
from test_appium.test_wechat.page.contacts_page import ContactsPage


class Main(BasePage):
    def goto_contacts_page(self):
        self.find_click((MobileBy.XPATH, '//*[@text="通讯录"]'))
        return ContactsPage(self._driver)
