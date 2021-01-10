#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from time import sleep
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from test_selenium.base import Base


class TestFile(Base):
    # @pytest.mark.skip
    def test_file(self):
        self.driver.get('https://image.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id('stfile').send_keys(r'D:\Hogwarts\test_selenium\tupian.png')
        sleep(5)


