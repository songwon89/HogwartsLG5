#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from test_pageobject.page.base_page import BasePage
from test_pageobject.page.login import Login
from test_pageobject.page.register import Register


class Main(BasePage):
    _base_ulr = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self._driver)
