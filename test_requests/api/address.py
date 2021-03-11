#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

from test_requests.api.base import Base


class Address(Base):

    def add_member(self, user_id, name, mobile):
        body = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            "department": [1]
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        return self.send("post", url, json=body)

    def update_member(self, user_id, name):
        body = {
            "userid": user_id,
            "name": name,
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        return self.send("post", url, json=body)

    def delete_member(self, user_id):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={user_id}"
        return self.send("get", url)

    def get_member(self, user_id):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={user_id}"
        return self.send("get", url)
