#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 03/02/2018 3:09 PM
# @Author  : Lee
# @File    : quick_sort_3_ways.py
# @Software: PyCharm

import random

from utils.common import swap
from utils.sort_test_helper import SortTestHelper


class QuickSort3Ways(object):

    @classmethod
    def sort(cls, lists, *args):
        if len(args):
            left = args[0]
            right = args[1]
            if left >= right:
                return

            swap(lists, left, int(random.random() * (right - left + 1)) + left)
            base = lists[left]

            """
            lists[left+1...lt] < v
            lists[gt...right] > v
            lists[lt+1...i) == v
            保证初始化的三个区间全部为空
            后续相应元素逐个添加进去
            """
            lt = left
            gt = right + 1
            i = left + 1
            while i < gt:
                if lists[i] < base:
                    swap(lists, lt + 1, i)
                    lt += 1
                    i += 1
                elif lists[i] > base:
                    swap(lists, gt - 1, i)
                    gt -= 1
                else:
                    i += 1
            swap(lists, left, lt)
            cls.sort(lists, left, lt - 1)
            cls.sort(lists, gt, right)
        else:
            cls.sort(lists, 0, len(lists) - 1)


if __name__ == '__main__':
    test_lists = SortTestHelper.generate_random_list(1000000, 0, 1000000)
    SortTestHelper.test_sort(QuickSort3Ways, test_lists)
