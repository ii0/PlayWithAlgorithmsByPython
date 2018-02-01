#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 0:42
# @Author  : Lee
# @File    : bubble_sort.py
# @Software: PyCharm

from utils.common import swap
from utils.sort_test_helper import SortTestHelper


def bubble_sort(lists):
    length = len(lists)
    for i in range(length):
        for j in range(0, length - i - 1,):
            if lists[j] > lists[j+1]:
                swap(lists, j, j+1)
    return lists


if __name__ == '__main__':
    test_lists = SortTestHelper.generate_random_list(20, 0, 30)
    print(test_lists)
    bubble_sort(test_lists)
    print(test_lists)