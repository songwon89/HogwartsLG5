#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pytest
import yaml

from calculator.calculator import Calculator


def get_datas():
    with open("./test_data.yml") as f:
        datas = yaml.safe_load(f)
        data_add = datas["add"]
        data_sub = datas["sub"]
        data_mul = datas["mul"]
        data_div = datas["div"]
        return data_add, data_sub, data_mul, data_div


test_datas = get_datas()


class TestCalc:

    def setup_class(self):
        print("\n计算开始！\n")
        self.calc = Calculator()

    def teardown_class(self):
        print("\n计算结束！")

    @pytest.mark.parametrize("a, b, expect", test_datas[0])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        print(f"#########{result}")
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", test_datas[1])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", test_datas[2])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", test_datas[3])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert float('%.8f' % result) == float('%.8f' % expect)


if __name__ == '__main__':
    pytest.main("test_cal.py", "-v")
