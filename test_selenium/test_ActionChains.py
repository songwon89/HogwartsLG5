#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from test_selenium.base import Base


class TestActionChains(Base):

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        # Xpath两种形式定位
        # element_click = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        element_double_click = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        element_context_click = self.driver.find_element_by_xpath('/html/body/form/input[4]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_double_click)
        action.context_click(element_context_click)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_xpath('//span[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele).perform()
        sleep(3)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element_by_id('dragger')
        ele_drop = self.driver.find_element_by_xpath('/html/body/div[2]')
        action = ActionChains(self.driver)
        action.drag_and_drop(ele_drag, ele_drop).perform()
        # action.click_and_hold(ele_drag).release(ele_drop).perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele_uname1 = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele_uname2 = self.driver.find_element_by_xpath('/html/body/label[2]/table/tbody/tr/td[2]/input')
        action = ActionChains(self.driver)
        action.click(ele_uname1)
        action.send_keys('usernamee')
        action.send_keys(Keys.BACK_SPACE)
        # for i in range(5):
        #     action.send_keys(Keys.BACK_SPACE)
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).pause(1)
        action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)
        # action.click(ele_uname2)
        action.key_down(Keys.CONTROL, element=ele_uname2).send_keys('v').key_up(Keys.CONTROL)
        action.perform()
        sleep(3)
