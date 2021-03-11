#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest

from test_requests.api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize("user_id, name, mobile", [("666655", "lixiao", "13600012345"),
                                                       ("666677", "lixiao", "13600034567")])
    def test_add_member(self, user_id, name, mobile):
        self.address.delete_member(user_id)
        r = self.address.add_member(user_id, name, mobile)
        assert r.get("errcode") == 0
        r = self.address.get_member(user_id)
        assert r.get("userid") == user_id
