#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver import ActionChains, TouchActions

from test_selenium.base import Base


class TestActionChains(Base):

    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com")
        ele_input = self.driver.find_element_by_id('kw')
        ele_search = self.driver.find_element_by_id('su')
        ele_input.send_keys('selenium测试')
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()
        action.scroll_from_element(ele_search, 0, 10000).perform()
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)
