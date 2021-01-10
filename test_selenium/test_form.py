#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
from test_selenium.base import Base


class TestForm(Base):

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id('user_login').send_keys('123456')
        self.driver.find_element_by_id('user_password').send_keys('123456')
        self.driver.find_element_by_id('user_remember_me').click()
        sleep(3)
        self.driver.find_element_by_name('commit').click()
        sleep(3)

