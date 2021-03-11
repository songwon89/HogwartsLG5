#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests


class Base:
    def __init__(self):
        # 获取token
        corpid = "wwd3b8f6a82ca44c4f"
        corpsecret = "RBZ8_hsnRKTI0UvAQTBBwCVqRgaKQLMjZidWWnNq7l0"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url)
        self.access_token = r.json()['access_token']
        # 生命一个session
        self.s = requests.Session()
        # 将token放入到session中
        self.s.params = {"access_token": self.access_token}

    def send(self, *args, **kwargs):
        r = self.s.request(*args, **kwargs)
        return r.json()
