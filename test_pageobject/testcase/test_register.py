#!/usr/bin/env python
# -*- coding:utf-8 -*-
from test_pageobject.page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        assert self.main.goto_register().register()
        # assert self.main.goto_login().goto_register().register()
