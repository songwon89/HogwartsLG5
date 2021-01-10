#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_ulr = ""

    def __init__(self, driver: WebDriver = None):
        self._driver = ''
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._driver != '':
            self._driver.get(self._base_ulr)
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
