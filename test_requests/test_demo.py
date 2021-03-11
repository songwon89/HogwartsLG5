#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


def test_demo():
    # 获取token
    corpid = "wwd3b8f6a82ca44c4f"
    corpsecret = "RBZ8_hsnRKTI0UvAQTBBwGUay9WRL3d2n4d-6UGsMxg"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    r = requests.get(url)
    access_token = r.json()['access_token']

    # 读取成员
    user_id = "000011"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}&userid={user_id}"
    r = requests.get(url)
    # print(r.json())

    # 更新成员
    body = {
        "userid": "000011",
        "name": "李四啊啊",
    }
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={access_token}"
    r = requests.post(url, json=body)
    # print(r.json())

    # 创建成员
    body = {
        "userid": "999999",
        "name": "张三",
        "mobile": "+86 13800000000",
        "department": [1]
    }
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}"
    r = requests.post(url, json=body)
    # print(r.json())

    # 删除成员
    user_id = "999999"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={access_token}&userid={user_id}"
    r = requests.get(url)
    print(r.json())
