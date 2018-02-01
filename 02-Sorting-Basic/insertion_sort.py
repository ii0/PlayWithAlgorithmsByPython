#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 16:26
# @Author  : Lee
# @File    : insertion_sort.py
# @Software: PyCharm

from utils.common import swap
from utils.common import TEST_LISTS


def insertion_sort(lists):
    length = len(lists)

    for i in range(1, length):
        for j in range(i, 0, -1):
            if lists[j] < lists[j-1]:
                swap(lists, j, j-1)
            else:
                break
    return lists


if __name__ == '__main__':
    print(insertion_sort(TEST_LISTS))
