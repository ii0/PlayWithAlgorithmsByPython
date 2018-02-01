#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 0:03
# @Author  : Lee
# @File    : merge_sort_BU.py
# @Software: PyCharm

from copy import deepcopy

from utils.sort_test_helper import SortTestHelper


class MergeSortBU(object):
    """
    自底向上归并排序算法
    优化过程与merg_sort中方式一致
    """

    @staticmethod
    def merge(lists, left, mid, right):
        demo_lists = deepcopy(lists[left: right+1])
        left_point = left
        right_point = mid + 1
        for k in range(left, right + 1):
            if left_point > mid:
                lists[k] = demo_lists[right_point - left]
                right_point += 1
            elif right_point > right:
                lists[k] = demo_lists[left_point - left]
                left_point += 1
            elif demo_lists[left_point - left] < demo_lists[right_point - left]:
                lists[k] = demo_lists[left_point - left]
                left_point += 1
            else:
                lists[k] = demo_lists[right_point - left]
                right_point += 1

    @classmethod
    def sort(cls, lists, *args):
        # 将动态步长初始化为1
        step = 1
        length = len(lists)
        while step < length:
            i = 0
            while i < length - step:
                # 对lists[i...i+step-1]和lits[i+step...i+2*step-1]归并
                # 对于数组末尾边界条件需要进行判断是否越界，最大为length-1
                cls.merge(lists, i, i+step-1, min(i+step*2-1, length-1))
                i += 2 * step
            step *= 2


if __name__ == '__main__':
    test_lists = SortTestHelper.generate_random_list(10, 0, 1000)
    print(test_lists)
    SortTestHelper.test_sort(MergeSortBU, test_lists)
    print(test_lists)