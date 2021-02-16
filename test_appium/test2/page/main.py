#!/usr/bin/env python
# -*- coding:utf-8 -*-
from test_appium.test2.page.base_page import BasePage
from test_appium.test2.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yml")
        return Market(self._driver)
