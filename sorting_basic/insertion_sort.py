#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 16:26
# @Author  : Lee
# @File    : insertion_sort.py
# @Software: PyCharm

from utils.common import TEST_LISTS
from utils.common import swap


def insertion_sort(lists, *args):
    if len(args):
        for i in range(args[0] + 1, args[1]+1):
            for j in range(i, 0, -1):
                if lists[j] < lists[j-1]:
                    swap(lists, j, j-1)
                else:
                    break
    else:
        length = len(lists)
        for i in range(1, length):
            for j in range(i, 0, -1):
                if lists[j] < lists[j-1]:
                    swap(lists, j, j-1)
                else:
                    break
    return lists


def insertion_sort_plus(lists):
    """
    针对交换过程进行优化
    """
    length = len(lists)

    for i in range(1, length):
        temp = lists[i]
        j = i
        while j > 0 and temp < lists[j - 1]:
            lists[j] = lists[j - 1]
            j -= 1
        lists[j] = temp
    return lists


if __name__ == '__main__':
    # print(insertion_sort(TEST_LISTS))
    print(insertion_sort_plus(TEST_LISTS))
