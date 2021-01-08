#!/usr/bin/env python
# -*- coding:utf-8 -*-

nums = [2, 3, 5, 7, 8]
target = 13

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])