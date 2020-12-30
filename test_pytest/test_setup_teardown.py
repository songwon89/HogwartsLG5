#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pytest


def setup_module():
    print("\nsetup_module：当前模块执行前执行一次")


def teardown_module():
    print("\nteardown_module：当前模块执行后执行一次")


def setup_function():
    print("\nsetup_function：不在类中的用例执行前执行")


def teardown_function():
    print("\nteardown_function：不在类中的用例执行后执行")


def test_three():
    print("执行test three")


def test_four():
    print("执行test four")


class TestClass:
    def setup_class(self):
        print("\nsetup_class：类中所有用例执行前执行")

    def teardown_class(self):
        print("\nteardown_class：类中所有用例执行后执行")

    def setup_method(self):
        print("\nsetup_method：类中每个用例执行前执行")

    def teardown_method(self):
        print("\nteardown_method：类中每个用例执行后执行")

    def test_one(self):
        print("执行test one")

    def test_two(self):
        print("执行test two")
