#!/usr/bin/env python
# -*- coding:utf-8 -*-
import yaml


def handle_black(fun):
    def run(*args, **kwargs):
        instance = args[0]
        with open('../black_list.yaml', 'r', encoding='utf-8') as f:
            black_list = yaml.safe_load(f)
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            for black in black_list:
                eles = instance.driver.find_elements(*black)
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e
    return run
