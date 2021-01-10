#!/usr/bin/env python
# -*- coding:utf-8 -*-
from test_selenium.base import Base


class TestSelenium(Base):
    def test_selenium(self):
        self.driver.get("https://www.baidu.com/")
