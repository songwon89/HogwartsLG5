#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


def add_function(a, b):
    return a + b


# @pytest.mark.parametrize("a, b, expected", [(1, 3, 4), (-1, -2, -3), (-1.5, 1.5, 0)], ids=["int", "minus", "float"])
# def test_add(a, b, expected):
#     assert add_function(a, b) == expected


# 参数可以组合堆叠使用-》2*6获得6条测试用例
@pytest.mark.parametrize("a", [1, 3])
@pytest.mark.parametrize("b", [2, 5, 8])
def test_add(a, b):
    print(f"参数堆叠组合：a->{a}, b->{b}")