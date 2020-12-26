#!/usr/bin/env python
# -*- coding:utf-8 -*-
from test_python.src.chengyaojin import ChengYaoJin
from test_python.src.hero import Hero
from test_python.src.libai import LiBai
from test_python.src.log import log


class HeroFactory:
    @classmethod
    def creat_hero(cls, name: str) -> Hero:
        if name == '程咬金':
            return ChengYaoJin()
        elif name == '李白':
            return LiBai()
        else:
            log.error(f"Don't know how to create a hero")
            return None