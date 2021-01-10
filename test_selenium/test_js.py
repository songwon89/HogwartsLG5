#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from test_selenium.base import Base


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys("selenium测试")
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)
        for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))

    def test_time(self):
        self.driver.get("https://www.12306.cn/index/")
        sleep(3)
        froms = self.driver.find_element_by_xpath('//*[@id="fromStationText"]')
        tos = self.driver.find_element_by_xpath('//*[@id="toStationText"]')
        actions = ActionChains(self.driver)
        actions.click(froms).send_keys("广州南").send_keys(Keys.ENTER)
        actions.click(tos).send_keys("深圳北").send_keys(Keys.ENTER)
        actions.perform()
        self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        # self.driver.execute_script('a.removeAttribute("readonly")')
        self.driver.execute_script('''document.getElementById("train_date").value="2021-1-15"''')
        sleep(3)
        self.driver.find_element_by_id('search_one').click()
        sleep(10)
