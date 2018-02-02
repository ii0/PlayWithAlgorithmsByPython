#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 14:09
# @Author  : Lee
# @File    : quick_sort_2_ways.py
# @Software: PyCharm

import random

from utils.common import swap
from utils.sort_test_helper import SortTestHelper
from sorting_basic.insertion_sort import insertion_sort


class QuickSort2Ways(object):
    """
    双路快速排序算法
    针对存在大量重复键值的数组有大幅度性能优化
    partition过程：lists[left...p-1] < lists[p]; lists[p+1...right] > lists[p]
    """

    @staticmethod
    def partition(lists, left, right):
        # 随机标定点
        # lists[left...l] < base; lists[r...right] >= base
        swap(lists, left, int(random.random() * (right - left + 1)) + left)
        base = lists[left]

        l = left + 1
        r = right
        while True:
            while l <= right and lists[l] < base:
                l += 1
            while r >= left + 1 and lists[r] > base:
                r -= 1

            if l > r:
                break
            swap(lists, l, r)
            l += 1
            r -= 1
        """
        一次完整的遍历之后，l会停留在第一个大于base的位置，r会停留在第一个小于base的位置
        故将base的值与lists[r]进行交换，完成一次partition
        """
        swap(lists, left, r)
        return r

    @classmethod
    def sort(cls, lists, *args):
        if len(args):
            left = args[0]
            right = args[1]
            # if left >= right:
            #     return
            # 利用插入排序进行小数组范围优化
            if right - left <= 15:
                insertion_sort(lists, left, right)
                return
            p = cls.partition(lists, left, right)
            cls.sort(lists, left, p - 1)
            cls.sort(lists, p + 1, right)
        else:
            cls.sort(lists, 0, len(lists)-1)


if __name__ == '__main__':
    test_lists = SortTestHelper.generate_random_list(1000000, 0, 10000000)
    SortTestHelper.test_sort(QuickSort2Ways, test_lists)
