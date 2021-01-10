#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By
from test_pageobject.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, "corp_name").send_keys("name")
        self.find(By.ID, "manager_name").send_keys("managermane")
        sleep(3)
        return True
