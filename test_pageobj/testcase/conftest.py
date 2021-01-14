#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import pytest
import yaml

yaml_file_path = os.path.dirname(__file__) + "/test_data.yml"
with open(yaml_file_path, encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    data_add_member = datas["add_member"]
    data_add_member_fail = datas["add_member_fail"]
    data_add_department = datas["add_department"]


@pytest.fixture(params=data_add_member)
def get_data_add_member_datas(request):
    data = request.param
    return data


@pytest.fixture(params=data_add_member_fail)
def get_data_add_member_fail_datas(request):
    data = request.param
    return data


@pytest.fixture(params=data_add_department)
def get_data_add_department_datas(request):
    data = request.param
    return data
