#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, _base_driver=None):
        _base_driver: WebDriver
        if _base_driver is None:
            self.driver = webdriver.Chrome()
            if os.path.exists("../testcase/cookies.json"):
                try:
                    self.login_with_cookies()
                except Exception as e:
                    print(f'\n登录失败：{e}')
                    self.get_cookies()
            else:
                self.get_cookies()
        else:
            self.driver = _base_driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def login_with_cookies(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open("../testcase/cookies.json", 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        # self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

    def get_cookies(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 扫码登录后重新获得cookies
        self.driver.find_element_by_class_name("index_top_operation_loginBtn").click()
        sleep(20)
        cookies = self.driver.get_cookies()
        with open("../testcase/cookies.json", 'w') as f:
            json.dump(cookies, f)
            print("\n已重新保存cookies文件，请重新登录！")

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)
