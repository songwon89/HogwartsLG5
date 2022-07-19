#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


# fixture是pytest的一个外壳函数，可以模拟setup和teardown的操作
# yield之前的操作相当于setup，yield之后的操作相当于teardown
# yield相当于return，如果需要返回数据，直接放在yield后面
# 2种方法使用fixture，测试用例1和测试用例4

# 创建一个登录的fixture方法
@pytest.fixture()
def login():
    print("登录操作")
    print("获取token")
    uername = 'tom'
    password = '123456'
    token = 'token123456'
    yield uername, password, token
    print("登出操作")


# 测试用例1：需要提前登录
def test_case1(login):
    print(f"login username:{login[0]}, password:{login[1]}")
    print("测试用例1")


# 测试用例2：不需要提前登录
def test_case2(connectDB):
    print("测试用例2")


# 测试用例3：需要提前登录
def test_case3():
    print("测试用例3")


# 测试用例4：需要提前登录
@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")
