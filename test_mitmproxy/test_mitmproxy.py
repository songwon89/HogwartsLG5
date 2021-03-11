#!/usr/bin/env python
# -*- coding:utf-8 -*-
from mitmproxy import ctx
import mitmproxy.http


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)
        ctx.log.info("Base content %s" % str(flow.id))

    def response(self, flow: mitmproxy.http.HTTPFlow):
        ctx.log.info("Response %s" % str(flow))


# 将类添加到插件列表中
addons = [
    Counter()
]
