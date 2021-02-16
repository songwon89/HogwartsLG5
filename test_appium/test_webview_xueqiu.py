#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestDw:
    def setup(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '6.0',
                        'deviceName': 'emulator-5554',
                        'appPackage': 'com.xueqiu.android',
                        'appActivity': '.view.WelcomeActivityAlias',
                        'noReset': 'true',
                        # 'dontStopAppOnReset': 'true',
                        'skipDeviceInitialization': 'true',
                        'unicodeKeyBoard': 'true',
                        'resetKeyBoard': 'true'
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]').click()

