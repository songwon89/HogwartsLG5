#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import yaml

from test_appium.test_wechat.page.app import App


def get_data():
    with open('../data/data.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data['add']


@pytest.mark.parametrize("name, gender, phonenum", get_data())
class TestAddMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def teardown(self):
        self.app.stop()

    def test_add_member(self, name, gender, phonenum):
        toast_text = self.main.goto_contacts_page().goto_member_invite_page().goto_add_member_page()\
            .edit_name(name).edit_gender(gender).edit_phonenum(phonenum).click_save().get_toast_text()
        assert "添加成功" == toast_text
