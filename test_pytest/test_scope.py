#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


class TestDemo:
    def test_a(self, connectDB):
        print("TestDemo 测试用例a")

    def test_b(self):
        print("TestDemo 测试用例b")


class TestDemo2:
    def test_a(self):
        print("TestDemo2 测试用例a")

    def test_b(self):
        print("TestDemo2 测试用例b")
