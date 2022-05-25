#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


@pytest.fixture(scope="session")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库连接")


# 解决pytest执行结果case标题有中文时显示编码不正确
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('UTF-8').decode('unicode_escape')
        item._nodeid = item._nodeid.encode('UTF-8').decode('unicode_escape')
