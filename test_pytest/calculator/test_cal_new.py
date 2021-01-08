#!/usr/bin/env python
# -*- coding:utf-8 -*-
import allure
import pytest


@allure.feature("测试计算器")
class TestCalc:
    @allure.story("测试加法")
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_add_datas):
        result = None
        try:
            result = get_calc.add(get_add_datas[0], get_add_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_add_datas[2]

    @allure.story("测试除法")
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_div_datas):
        result = None
        try:
            result = get_calc.div(get_div_datas[0], get_div_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_div_datas[2]

    @allure.story("测试减法")
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_sub_datas):
        result = None
        try:
            result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_sub_datas[2]

    @allure.story("测试乘法")
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_mul_datas):
        result = None
        try:
            result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_mul_datas[2]
