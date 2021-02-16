#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver

from test_appium.test2.page.base_page import BasePage
from test_appium.test2.page.main import Main


class App(BasePage):
    def start(self):
        _package = 'com.xueqiu.android'
        _activity = '.view.WelcomeActivityAlias'
        if self._driver is None:
            desired_caps = {'platformName': 'Android',
                            'platformVersion': '6.0',
                            'deviceName': 'emulator-5554',
                            'appPackage': _package,
                            'appActivity': _activity,
                            'autoGrandPermissions': 'true'
                            }
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package)
        return self

    def main(self):
        return Main(self._driver)
