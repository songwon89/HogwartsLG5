#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


def test_a():
    # assert 1 == 2
    # assert False == True
    # assert 2 == 3
    pytest.assume(1 == 2)
    pytest.assume(True == True)
    pytest.assume(2 == 3)
