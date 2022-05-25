#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


# 通过传入request，使用request.param实现参数化
# ids 实现重命名用例名称
@pytest.fixture(params=[1, 2, 3], ids=['testcase r1', 'testcase r2', '测试用例 r3'])
def login1(request):
    data = request.param
    print("获取测试数据")
    return f"测试数据:{data}"


def test_case1(login1):
    print(login1)
    print("测试用例1")
