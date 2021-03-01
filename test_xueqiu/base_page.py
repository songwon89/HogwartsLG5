#!/usr/bin/env python
# -*- coding:utf-8 -*-
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_xueqiu.handle_black import handle_black


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 通过装饰器，过滤黑名单
    @handle_black
    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_click(self, locator):
        self.find(locator).click()

    def find_send(self, locator, contant):
        self.find(locator).send_keys(contant)

    def scroll_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                 'scrollable(true).instance(0)).'
                                                 'scrollIntoView(new UiSelector().'
                                                 f'text("{text}").instance(0));')
        self.find_click(element)

    def find_get_text(self, result):
        return self.find(result).text

    def run_steps(self, path, operation):
        with open(path, 'r', encoding='utf-8') as f:
            datas = yaml.safe_load(f)
        steps = datas[operation]
        for step in steps:
            action = step['action']
            if action == 'find_click':
                self.find_click(step['locator'])
            elif action == 'find_send':
                self.find_send(step['locator'], step['content'])
