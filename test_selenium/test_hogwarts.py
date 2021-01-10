#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from test_selenium.base import Base


class TestHogwarts(Base):

    def test_hogwarts(self):
        self.driver.get("https://testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()
        time.sleep(3)
