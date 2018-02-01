#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 16:03
# @Author  : Lee
# @File    : common.py
# @Software: PyCharm


TEST_LISTS = [10, 8, 9, 7, 5, 3, 2, 1, 100]


def swap(lists, i, j):
    lists[i], lists[j] = lists[j], lists[i]