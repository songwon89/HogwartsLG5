#!/usr/bin/env python
# -*- coding:utf-8 -*-

import allure
import pytest


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>", "html测试块", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file("./123.png", "这是一张图片", attachment_type=allure.attachment_type.PNG)
