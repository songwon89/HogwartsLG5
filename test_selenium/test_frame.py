#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains

from test_selenium.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        ele_drag = self.driver.find_element_by_id('draggable')
        ele_drop = self.driver.find_element_by_id('droppable')
        # action = ActionChains(self.driver)
        # action.drag_and_drop(ele_drag, ele_drop).perform()
        # sleep(3)
        self.driver.switch_to.parent_frame()
        # self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
        # self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
