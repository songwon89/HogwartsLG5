#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys

from selenium import webdriver


class Base:
    def setup(self):
        browser = os.getenv('browser')
        # browser = sys.argv()
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        else:
            opt = webdriver.ChromeOptions()
            opt.add_experimental_option('w3c', False)
            self.driver = webdriver.Chrome(chrome_options=opt)
        # self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
