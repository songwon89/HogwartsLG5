#!/usr/bin/env python
# -*- coding:utf-8 -*-
from test_appium.test_wechat.page.base_page import BasePage
from test_appium.test_wechat.page.memberinvite_page import MemberInvitePage


class ContactsPage(BasePage):
    def goto_member_invite_page(self):
        self.scroll_click("添加成员")
        return MemberInvitePage(self._driver)
