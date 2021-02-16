#!/usr/bin/env python
# -*- coding:utf-8 -*-

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDw:
    def setup(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '6.0',
                        'deviceName': 'emulator-5554',
                        'appPackage': 'com.tencent.wework',
                        'appActivity': '.launch.LaunchSplashActivity',
                        'noReset': 'true',
                        'skipDeviceInitialization': 'true',
                        'unicodeKeyBoard': 'true',
                        'resetKeyBoard': 'true',
                        'ensureWebviewHavaPages': 'true',
                        'settings[waitForIdleTimeout]': 0  # 设置页面等待空闲状态的时间为0秒
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        name = '张三七'
        gender = '男'
        phonenum = '13011111143'
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,  # 添加成员按钮不在第一屏时，滑动查找
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(name)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        locator = (MobileBy.XPATH, '//*[@text="女"]')
        # 显式等待，等待性别选项弹出
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        if gender == '女':
            self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        else:
            self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fwi').send_keys(phonenum)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/aj_').click()
        # 获取toast提示内容
        toast_text = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert "添加成功" == toast_text
