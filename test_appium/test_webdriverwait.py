#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


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

    def test_wait(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()
        locator = (MobileBy.XPATH,
                   "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # ele = self.driver.find_element(*locator)
        # c_price = float(ele.text)
        # print(f'current price: {c_price}')
        # assert c_price > 200

        ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        c_price = float(ele.text)
        print(f'current price: {c_price}')
        assert c_price > 200
