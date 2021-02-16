#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast:
    def setup(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '6.0',
                        'deviceName': 'emulator-5554',
                        'appPackage': 'com.touchboarder.android.api.demos',
                        'appActivity': 'com.example.android.apis.view.PopupMenu1',
                        'noReset': 'true',
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="Make a Popup!"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="Search"]').click()
        # 打印当前页面的dom树
        # print(self.driver.page_source)

        # 获取toast内容的两种方法
        print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)
        print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "Clicked popup")]').text)
