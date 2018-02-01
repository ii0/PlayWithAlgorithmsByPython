#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 21:24
# @Author  : Lee
# @File    : merge_sort.py
# @Software: PyCharm

from copy import deepcopy

from utils.sort_test_helper import SortTestHelper
from sorting_basic.insertion_sort import insertion_sort

class MergeSort(object):

    @staticmethod
    def merge(lists, left, mid, right):
        """

        :param lists: 当前需要归并的小数组
        :param left: 数组的当前最小的索引值
        :param mid: 数组中间索引值
        :param right: 数组最大的索引值
        :return:
        由于索引值在lists是固定的，故在归并过程需要取偏移量进行计算
        """
        demo_lists = deepcopy(lists[left: right+1])
        left_point = left
        right_point = mid + 1
        for k in range(left, right+1):
            # 左半边元素已处理完
            if left_point > mid:
                lists[k] = demo_lists[right_point -left]
                right_point += 1
            # 右半边元素已处理完
            elif right_point > right:
                lists[k] = demo_lists[left_point - left]
                left_point += 1
            # 左指针对应元素小于右指针对应元素
            elif demo_lists[left_point - left] < demo_lists[right_point - left]:
                lists[k] = demo_lists[left_point - left]
                left_point += 1
            # 左指针对应元素大于右指针对应元素
            else:
                lists[k] = demo_lists[right_point - left]
                right_point += 1

    @classmethod
    def sort(cls, lists, *args):
        if len(args):
            left = args[0]
            right = args[1]
            if left >= right:
                return
            """
            优化2：对于小规模数组，使用插入排序
            """
            if right - left <= 15:
                insertion_sort(lists)

            mid = int((left + right) / 2)
            cls.sort(lists, left, mid)
            cls.sort(lists, mid + 1, right)
            cls.merge(lists, left, mid, right)

            """
            优化1: 对于lists[mid] <= lists[mid + 1]的情况, 不进行merge
            对于近乎有序的数组非常有效, 但是对于一般情况, 有一定的性能损失
            """
            # if lists[mid] > lists[mid+1]:
            #     cls.merge(lists, left, mid, right)
        else:
            cls.sort(lists, 0, len(lists)-1)


if __name__ == '__main__':
    test_lists = SortTestHelper.generate_random_list(10000, 0, 100000)
    SortTestHelper.test_sort(MergeSort, test_lists)
