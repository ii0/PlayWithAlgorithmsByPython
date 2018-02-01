#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 1:09
# @Author  : Lee
# @File    : quick_sort.py
# @Software: PyCharm

from utils.common import swap
from utils.sort_test_helper import SortTestHelper


class QuickSort(object):

    @staticmethod
    def partition(lists, left, right):
        """
        选取第一个元素为标定点
        lists[left+1...k] < base; lists[k+1...right] > base
        :param lists:
        :param left:
        :param right:
        :return:
        """
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
    test_lists = SortTestHelper.generate_random_list(100000, 0, 1000000)
    SortTestHelper.test_sort(QuickSort, test_lists)