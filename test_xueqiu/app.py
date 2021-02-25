#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver

from test_xueqiu.base_page import BasePage
from test_xueqiu.page.main import MainPage


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        if self.driver is None:
            desired_caps = {'platformName': 'Android',
                            'platformVersion': '6.0',
                            'deviceName': 'emulator-5554',
                            'appPackage': _package,
                            'appActivity': _activity,
                            'noReset': 'true',
                            'autoGrandPermissions': 'true'
                            }
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def main(self):
        return MainPage(self.driver)
