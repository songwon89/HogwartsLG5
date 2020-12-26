#!/usr/bin/env python
# -*- coding:utf-8 -*-
from unittest import TestCase

from test_python.src.hero_factory import HeroFactory


class TestHero(TestCase):
    def test_fight(self):
        # chengyaojin = ChengYaoJin()
        # libai = LiBai()
        chengyaojin = HeroFactory.creat_hero("程咬金")
        libai = HeroFactory.creat_hero("李白")
        assert chengyaojin.fight(libai) == True
        # chengyaojin = ChengYaoJin()
        # libai = LiBai()
        chengyaojin = HeroFactory.creat_hero("程咬金")
        libai = HeroFactory.creat_hero("李白")
        assert libai.fight(chengyaojin) == False
