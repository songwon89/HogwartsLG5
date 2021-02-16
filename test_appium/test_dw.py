#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDw:
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
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        sleep(3)
        self.driver.quit()

    @pytest.mark.skip
    def test_search(self):
        """
        1. 打开 雪球 app
        2. 点击搜索输入框
        3. 输入 “阿里巴巴”
        4. 在搜索结果里选择“阿里巴巴”， 点击
        5. 获取股票价格， 判断价格是否>200
        :return:
        """
        print('搜索测试用例')

        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        print(current_price)
        assert current_price > 200

    @pytest.mark.skip
    def test_attr(self):
        ele_search = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        enabled_search = ele_search.is_enabled()
        print(ele_search.text)
        print(ele_search.location)
        print(ele_search.size)
        if enabled_search:
            ele_search.click()
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
            ele_ali = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            enabled_ali = ele_ali.get_attribute('displayed')
            if enabled_ali == 'true':
                print('搜索成功')
                ele_ali.click()
            else:
                print('搜索失败')

    @pytest.mark.skip
    def test_touchaction(self):
        # sleep(3)
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_s = int(height * 0.8)
        y_e = int(height * 0.2)
        action.press(x=x1, y=y_s).wait(900).move_to(x=x1, y=y_e).release().perform()

    @pytest.mark.skip
    def test_get_current(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        c_price = self.driver.find_element_by_xpath(
            "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        assert float(c_price) > 200

    @pytest.mark.skip
    def test_myinfo(self):
        """
        1. 点击我的，进入到个人信息界面
        2. 点击登录，进入登录界面
        3.输入用户名，密码
        4. 点击登录
        :return:
        """
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("我的").fromParent(resourceId("com.xueqiu.android:id/tab_icon"))').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    def test_scroll_find(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance('
                                                        '0)).scrollIntoView(new UiSelector().text("朱酒").instance('
                                                        '0));').click()
        sleep(5)
