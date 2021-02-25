#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator):
        element = self._driver.find_element(*locator)
        return element

    def find_click(self, locator):
        self.find(locator).click()

    def find_send_keys(self, locator, contant):
        self.find(locator).send_keys(contant)

    def scroll_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                 'scrollable(true).instance(0)).'
                                                 'scrollIntoView(new UiSelector().'
                                                 f'text("{text}").instance(0));')
        self.find_click(element)

    def find_get_text(self, result):
        return self.find(result).text
