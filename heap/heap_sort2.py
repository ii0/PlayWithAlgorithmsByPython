#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 05/02/2018 12:50 AM
# @Author  : Lee
# @File    : heap_sort2.py
# @Software: PyCharm

from heap.max_heap import MaxHeap


def heap_sort2(lists):
    """
    通过heapify进行建堆，时间复杂度为O(n)
    相对于heap_sort1性能有优化
    :param lists:
    :return:
    """
    length = len(lists)
    max_heap = MaxHeap(lists)
    for i in range(length - 1, -1, -1):
        lists[i] = max_heap.extract_max()
    return lists


if __name__ == '__main__':
    test_lists = [1, 3, 5, 7, 2, 4, 6, 8, 10, 99, 100]
    print(heap_sort2(test_lists))