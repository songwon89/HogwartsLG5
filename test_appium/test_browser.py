#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestGetAttr:
    def setup(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '6.0',
                        'deviceName': 'emulator-5554',
                        'browserName': 'Browser',
                        'noResrt': 'true',
                        # 'chromedriverExecutable': '指定driver地址，如果放在默认地址，不用加此内容'
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id('index-kw').click()
        self.driver.find_element_by_id('index-kw').send_keys('appium')
        ele_search = (By.ID, 'index-bn')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ele_search))
        self.driver.find_element(*ele_search).click()
        sleep(5)
