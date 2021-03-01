#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from test_xueqiu.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        self.run_steps('../page/search_page.yaml', 'search')
        # self.find_send((MobileBy.ID, 'com.xueqiu.android:id/search_input_text'), 'alibaba')
        # self.find_click((MobileBy.XPATH, '//*[@text="阿里巴巴-SW"]'))
        return True
