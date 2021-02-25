#!/usr/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.test_wechat.page.base_page import BasePage


class AddMemberPage(BasePage):
    def edit_name(self, name):
        self.find_send_keys((MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText'), name)
        return self

    def edit_gender(self, gender):
        self.find_click((MobileBy.XPATH, '//*[@text="男"]'))
        locator = (MobileBy.XPATH, '//*[@text="女"]')
        # 显式等待，等待性别选项弹出
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        if gender == '女':
            self.find_click((MobileBy.XPATH, '//*[@text="女"]'))
        else:
            self.find_click((MobileBy.XPATH, '//*[@text="男"]'))
        return self

    def edit_phonenum(self, phonemum):
        self.find_send_keys((MobileBy.ID, 'com.tencent.wework:id/fwi'), phonemum)
        return self

    def click_save(self):
        from test_appium.test_wechat.page.memberinvite_page import MemberInvitePage
        self.find_click((MobileBy.ID, 'com.tencent.wework:id/aj_'))
        return MemberInvitePage(self._driver)
