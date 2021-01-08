#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


@pytest.mark.run(order=2)
# @pytest.mark.second
def test_a():
    print('11111111')


@pytest.mark.run(order=1)
# @pytest.mark.first
def test_b():
    print('222222222')
