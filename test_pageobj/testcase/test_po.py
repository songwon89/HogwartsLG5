#!/usr/bin/env python
# -*- coding:utf-8 -*-
from time import sleep

from test_pageobj.page.main_page import MainPage


class TestPo:
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        sleep(5)
        self.main.driver.quit()

    def test_add_member(self, get_data_add_member_datas):
        result = self.main.goto_contact().goto_add_member().add_menber(*get_data_add_member_datas).get_member_list()
        assert get_data_add_member_datas[0] in result

    def test_add_member_fail(self, get_data_add_member_fail_datas):
        """
        帐号及手机必须唯一，不可以重复
        :return:
        """
        error_tips = self.main.goto_contact().goto_add_member().add_member_fail(*get_data_add_member_fail_datas)
        assert error_tips == f'该手机号已被张三占有'

    def test_add_department(self, get_data_add_department_datas):
        result = self.main.goto_contact().goto_add_department().add_department(get_data_add_department_datas).get_department_list()
        assert get_data_add_department_datas in result

    def test_add_department_fail(self, get_data_add_department_datas):
        sleep(10)
        error_tips, department_list = self.main.goto_contact().goto_add_department().add_department_fail(get_data_add_department_datas)
        assert error_tips == '该部门已存在' and department_list.count(get_data_add_department_datas) == 1
