#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04/02/2018 5:22 PM
# @Author  : Lee
# @File    : heap_sort1.py
# @Software: PyCharm

from heap.max_heap import MaxHeap


def heap_sort1(lists):
    """
    创建一个空堆
    然后将元素逐个insert进去
    然后倒序取出存入列表
    时间复杂度为O(nlogn)
    :param lists:
    :return:
    """
    length = len(lists)
    max_heap = MaxHeap(length)
    for i in range(length):
        max_heap.insert(lists[i])

    for i in range(length - 1, -1, -1):
        lists[i] = max_heap.extract_max()
    return lists


if __name__ == '__main__':
    test_lists = [1, 3, 5, 7, 2, 4, 6, 8, 10, 99, 100]
    print(heap_sort1(test_lists))
