#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from test_xueqiu.base_page import BasePage
from test_xueqiu.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        self.find_click((MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]'))
        self.find_click((MobileBy.XPATH, '//*[@text="行情"]'))
        return MarketPage(self.driver)
