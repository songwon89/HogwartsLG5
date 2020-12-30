#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import yaml


class TestData:
    @pytest.mark.parametrize("a, b", yaml.safe_load(open("data.yml")))
    def test_data(self, a, b):
        print(a+b)

    def test_y(self):
        print(yaml.safe_load(open("data.yml")))