#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver

from test_appium.test_wechat.page.base_page import BasePage
from test_appium.test_wechat.page.main import Main


class App(BasePage):
    def start(self):
        _package = 'com.tencent.wework'
        _activity = '.launch.WwMainActivity'
        if self._driver is None:
            desired_caps = {'platformName': 'Android',
                            'platformVersion': '6.0',
                            'deviceName': 'emulator-5554',
                            'appPackage': _package,
                            'appActivity': _activity,
                            'noReset': 'true',
                            'autoGrandPermissions': 'true'
                            }
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package)
        return self

    def restart(self):
        self._driver.quit()
        self._driver.launch_app()
        return self

    def stop(self):
        self._driver.quit()
        return self

    def main(self):
        return Main(self._driver)
