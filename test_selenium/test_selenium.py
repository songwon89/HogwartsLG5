#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver


class TestSelenium:
    def setup(self):
        # browser = os.getenv('browser')
        # # browser = sys.argv()
        # if browser == 'firefox':
        #     self.driver = webdriver.Firefox()
        # elif browser == 'headless':
        #     self.driver = webdriver.PhantomJS()
        # elif browser == 'edge':
        #     self.driver = webdriver.Edge()
        # else:
        #     opt = webdriver.ChromeOptions()
        #     opt.add_experimental_option('w3c', False)
        #     self.driver = webdriver.Chrome(chrome_options=opt)
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.get("https://www.baidu.com/")
        sleep(3)
