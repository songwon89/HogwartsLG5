#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            print(f"测试环境IP：{env['test']}")
        elif "dev" in env:
            print("这是测试环境")
            print(f"开发环境IP：{env['dev']}")

    def test_yaml(self):
        print(yaml.safe_load(open("./env.yml")))
