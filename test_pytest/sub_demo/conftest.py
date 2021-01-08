#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


@pytest.fixture()
def connectDB():
    print("这是sub_demo下的connectDB")