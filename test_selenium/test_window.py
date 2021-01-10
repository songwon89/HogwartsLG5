#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from test_selenium.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_link_text('立即注册').click()
        c_window = self.driver.current_window_handle
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(3)
        self.driver.switch_to.window(c_window)
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('123')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('password')
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(3)
