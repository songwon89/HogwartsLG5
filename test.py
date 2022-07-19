#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest

"""
在面试的时候有一道算法题，要求编写一个函数，判断一个给定的字符串s，能否可以由另外两个子串part1和part2合成。 注意，part1和part2中的字母原有顺序必须和s中出现的顺序是一致的。

【示例】
输入：s='hogwarts', part1='hws', part2='ogart'
输出：True
解释：因为hws和ogart的出现顺序和hogwarts一致，合成后也是hogwarts，因此是True

题目难度：困难
"""


def solution(s: str, part1: str, part2: str) -> bool:
    for i in s:
        if i in part1:
            part1 = part1.replace(i, '', 1)
            s = s.replace(i, '', 1)
        elif i in part2:
            part2 = part2.replace(i, '', 1)
            s = s.replace(i, '', 1)
    print(s, part1, part2)
    if s == part1 == part2:
        return True
    else:
        return False


if __name__ == '__main__':
    print(solution('hogwarts', 'hws', 'ogart'))
    print(solution('codeewars', 'codee', 'wars'))
    print(solution('codewars', 'cod', 'wars'))
    print(solution('haahheihei', 'haheihei', 'ha'))
    # assert solution('hogwarts', 'hws', 'ogart') is True
    # assert solution('codewars', 'code', 'wars') is True
    # assert solution('codewars', 'cod', 'wars') is False
