#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
import os

from test_selenium.base import Base


class TestBaidu(Base):

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element_by_id('su').click()
        sleep(4)
