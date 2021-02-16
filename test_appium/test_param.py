#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDw:
    def setup_class(self):
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

    def teardown_class(self):
        pass
        # self.driver.quit()

    @pytest.mark.parametrize('name, _type, expect_price', [
        ('alibaba', 'BABA', 200),
        ('小米', '01810', 25)
    ])
    def test_search(self, name, _type, expect_price):
        """
        1. 点击输入框
        2. 输入 alibaba or xiaomi
        3. 点击第一个搜索结果
        4. 判断股票价格
        :return:
        """
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(name)
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name"]').click()
        current_price = self.driver.find_element(MobileBy.XPATH, f'//*[@text="{_type}"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        print(f'\n当前价格：{current_price} 预期价格：{expect_price}\n')
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()
