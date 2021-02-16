#!/usr/bin/env python
# -*- coding:utf-8 -*-
from test_appium.test2.page.base_page import BasePage
from test_appium.test2.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yml")
        return Search(self._driver)
