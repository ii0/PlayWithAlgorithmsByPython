#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 1:43
# @Author  : Lee
# @File    : random_quick_sort.py
# @Software: PyCharm

import random

from utils.common import swap
from utils.sort_test_helper import SortTestHelper


class RandomQuickSort(object):

    @staticmethod
    def partition(lists, left, right):
        """
        对于普通快排，若排序数组为近乎有序的
        每次选取第一个元素为标定点则会将算法时间复杂度往O（n*2）提高，接近于最坏的处理情况
        这种处理场景，随机快排能大幅度降低时间复杂度
        lists[left+1...k] < base; lists[k+1...right] > base

        """
        swap(lists, left, int(random.random() * (right - left + 1)) + left)
        base = lists[left]
        k = left
        for i in range(left+1, right+1):
            if base > lists[i]:
                k += 1
                swap(lists, k, i)
        swap(lists, left, k)
        return k

    @classmethod
    def sort(cls, lists, *args):
        if len(args):
            left = args[0]
            right = args[1]
            if left >= right:
                return

            p = cls.partition(lists, left, right)
            cls.sort(lists, left, p-1)
            cls.sort(lists, p+1, right)

        else:
            cls.sort(lists, 0, len(lists) - 1)

if __name__ == '__main__':
    test_lists = SortTestHelper.generate_near_ordered_list(100000, 100)
    SortTestHelper.test_sort(RandomQuickSort, test_lists)