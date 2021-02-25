#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_wechat.page.addmember_page import AddMemberPage
from test_appium.test_wechat.page.base_page import BasePage


class MemberInvitePage(BasePage):
    def goto_add_member_page(self):
        self.find_click((MobileBy.XPATH, '//*[@text="手动输入添加"]'))
        return AddMemberPage(self._driver)

    def get_toast_text(self):
        result = self.find_get_text((MobileBy.XPATH, '//*[contains(@text,"添加成功")]'))
        return result
