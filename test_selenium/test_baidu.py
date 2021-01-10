#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
import os

from selenium.webdriver.common.by import By

from test_selenium.base import Base


class TestBaidu(Base):

    def test_baidu(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        self.driver.find_element(By.ID, 'corp_name').send_keys("name")
        # self.driver.get("https://www.baidu.com")
        # self.driver.find_element_by_id('kw').send_keys("霍格沃兹测试学院")
        # self.driver.find_element_by_id('su').click()
        sleep(4)
