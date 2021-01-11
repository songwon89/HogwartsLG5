#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
from time import sleep
from selenium import webdriver


class TestCookies:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_cookies(self):
        if os.path.exists("./cookies.json"):
            try:
                self.login_with_cookies()
            except Exception as e:
                print(f'登录失败：{e}')
                self.get_cookies()
        else:
            self.get_cookies()

    def get_cookies(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 扫码登录后重新获得cookies
        self.driver.find_element_by_class_name("index_top_operation_loginBtn").click()
        sleep(20)
        cookies = self.driver.get_cookies()
        with open("./cookies.json", 'w') as f:
            json.dump(cookies, f)
            print("\n已重新保存cookies文件，请重新登录！")

    def login_with_cookies(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open("./cookies.json", 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(1)
        self.driver.find_element_by_id("menu_customer").click()
        sleep(3)
