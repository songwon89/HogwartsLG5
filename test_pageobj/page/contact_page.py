#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from test_pageobj.page.base_page import BasePage


class ContactPage(BasePage):
    def goto_add_member(self):
        sleep(1)
        self.find(By.CSS_SELECTOR, '[class="ww_operationBar"] .js_add_member').click()
        return AddMemberPage(self.driver)

    def goto_add_department(self):
        sleep(1)
        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        return AddDepartmentPage(self.driver)

    def get_member_list(self):
        sleep(1)
        member_weblist = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        member_list = []
        for member in member_weblist:
            member_list.append(member.text)
        return member_list

    def get_department_list(self):
        sleep(1)
        department_weblist = self.driver.find_elements(By.CSS_SELECTOR, '.jstree-leaf')
        department_list = []
        for department in department_weblist:
            department_list.append(department.text.strip())
        return department_list


class AddMemberPage(BasePage):
    def add_menber(self, name, acctid, phone):
        self.find(By.ID, 'username').send_keys(name)
        self.find(By.ID, 'memberAdd_acctid').send_keys(acctid)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return ContactPage(self.driver)

    def add_member_fail(self, name, acctid, phone):
        self.find(By.ID, 'username').send_keys(name)
        self.find(By.ID, 'memberAdd_acctid').send_keys(acctid)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(1)
        error_tips = self.find(By.CSS_SELECTOR, '.ww_telInput+.ww_inputWithTips_tips').text
        return error_tips


class AddDepartmentPage(BasePage):
    def add_department(self, department_name):
        self.find(By.CSS_SELECTOR, '[name="name"]').send_keys(department_name)
        self.find(By.CSS_SELECTOR, '.js_toggle_party_list').click()
        self.find(By.CSS_SELECTOR, '.ww_dialog_body [id="1688854063688237_anchor"]').click()
        self.find(By.CSS_SELECTOR, '[d_ck="submit"]').click()
        return ContactPage(self.driver)

    def add_department_fail(self, department_name):
        self.find(By.CSS_SELECTOR, '[name="name"]').send_keys(department_name)
        self.find(By.CSS_SELECTOR, '.js_toggle_party_list').click()
        self.find(By.CSS_SELECTOR, '.ww_dialog_body [id="1688854063688237_anchor"]').click()
        self.find(By.CSS_SELECTOR, '[d_ck="submit"]').click()
        sleep(1)
        error_tips = self.find(By.CSS_SELECTOR, '.ww_tip.error.ww_tip_Warning').text
        department_list = ContactPage(self.driver).get_department_list()
        return error_tips, department_list
