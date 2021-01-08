#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import pytest
import yaml

from calculator.calculator import Calculator

yaml_file_path = os.path.dirname(__file__) + "/test_data.yml"
with open(yaml_file_path, encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    data_add = datas["add"]
    data_sub = datas["sub"]
    data_mul = datas["mul"]
    data_div = datas["div"]
    add_ids = datas["add_ids"]
    sub_ids = datas["sub_ids"]
    mul_ids = datas["mul_ids"]
    div_ids = datas["div_ids"]


@pytest.fixture(params=data_add, ids=add_ids)
def get_add_datas(request):
    data = request.param
    return data


@pytest.fixture(params=data_sub, ids=sub_ids)
def get_sub_datas(request):
    data = request.param
    return data


@pytest.fixture(params=data_mul, ids=mul_ids)
def get_mul_datas(request):
    data = request.param
    return data


@pytest.fixture(params=data_div, ids=div_ids)
def get_div_datas(request):
    data = request.param
    return data


@pytest.fixture(scope="module")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("\n结束计算")
