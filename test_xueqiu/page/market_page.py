#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from test_xueqiu.base_page import BasePage
from test_xueqiu.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search_page(self):
        self.run_steps('../page/market_page.yaml', 'goto_search_page')
        # self.find_click((MobileBy.ID, 'com.xueqiu.android:id/action_search'))
        return SearchPage(self.driver)
