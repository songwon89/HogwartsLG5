#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

import pytest


def test_rerun():
    sleep(1)
    assert 1 == 1


def test_rerun1():
    sleep(1)
    assert 1 == 3


# 通过装饰器重跑失败用例
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_rerun2():
    sleep(1)
    assert 1 == 4
