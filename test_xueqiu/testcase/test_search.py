#!/usr/bin/env python
# -*- coding:utf-8 -*-
from test_xueqiu.app import App


def test_search():
    app = App()
    result = app.start().main().goto_market_page().goto_search_page().search()
    assert result
