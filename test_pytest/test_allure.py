#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pytest


def test_success():
    """this test succeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip("for a second!")


def test_broken():
    raise Exception('oops')
