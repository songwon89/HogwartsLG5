#!/usr/bin/env python
# -*- coding:utf-8 -*-

def b(fun):
    def run(*args, **kwargs):
        print('before a')
        fun(*args, **kwargs)
        print('after a')
    return run


@b
def a():
    print('a')


def test_demo():
    a()
