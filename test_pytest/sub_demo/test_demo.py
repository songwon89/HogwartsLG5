#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


@pytest.fixture()
def connectDB():
    print("test_demo下的connectDB")


def test_a(connectDB):
    print("sub_demo test_a")


class TestB:
    def test_b(self):
        print("sub_demo test_b")
