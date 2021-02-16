#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestGetAttr:
    def setup(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '6.0',
                        'deviceName': 'emulator-5554',
                        'appPackage': 'com.xueqiu.android',
                        'appActivity': '.view.WelcomeActivityAlias',
                        'noResrt': 'true',
                        # 'dontStopAppOnReset': 'true',
                        'skipDeviceInitialization': 'true',
                        'unicodeKeyBoard': 'true',
                        'resetKeyBoard': 'true'
                        }
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        # self.driver.quit()
        pass

    @pytest.mark.skip
    def test_get_attri(self):
        ele_search = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        print(ele_search.get_attribute("content-desc"))
        print(ele_search.get_attribute("resource-id"))
        print(ele_search.get_attribute("clickable"))
        print(ele_search.get_attribute("enabled"))
        print(ele_search.get_attribute("bounds"))

    def test_hamcrest(self):
        assert_that(10, equal_to(10))
        # 13不在10+-2的范围内
        assert_that(13, close_to(10, 2))
        assert_that("contains some string", contains_string("string"))
