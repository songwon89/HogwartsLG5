#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from test_pageobj.page.base_page import BasePage
from test_pageobj.page.contact_page import ContactPage, AddMemberPage


class MainPage(BasePage):
    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)
