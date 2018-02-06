#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 05/02/2018 11:49 PM
# @Author  : Lee
# @File    : heap_sort.py
# @Software: PyCharm

from utils.sort_test_helper import SortTestHelper


class HeapSort(object):
    """
    这种堆排序不在调用最大堆的数据结构
    直接在原数组上进行shift_down操作完成堆排序
    BTW:最大堆在实现上，数组从1开始索引，此处数组则从0开始索引
    故需要注意边界条件
    """
    @classmethod
    def sort(cls, lists):
        """
        由于这种实现是从0开始索引
        所以最后一个非叶子节点为(count-1)/2
        即：(length - 1 - 1)/2
        """
        length = len(lists)
        for i in range((length - 1 - 1)//2, -1, -1):
            cls.shift_down(lists, length - 1, i)

        for i in range(length - 1, 0, -1):
            cls.swap(lists, i, 0)
            cls.shift_down(lists, i-1, 0)

    @staticmethod
    def swap(lists, i, j):
        lists[i], lists[j] = lists[j], lists[i]

    @classmethod
    def shift_down(cls, lists, count, k):
        """
            k
           /\
          / \
       2K+1 2K+2
        :param lists: 堆
        :param count: 堆大小
        :param k: 节点位置（从0索引）
        :return:
        """
        while 2 * k + 1 <= count:
            j = 2 * k + 1
            # 判断是否存在右子树并且进行左右子树比较
            if j + 1 <= count and lists[2*k + 1] < lists[2*k + 2]:
                j += 1

            if lists[k] < lists[j]:
                cls.swap(lists, k, j)
                k = j
            else:
                break


if __name__ == '__main__':
    test_lists = [1, 3, 5, 7, 2, 4, 6, 8, 10, 99, 100]
    SortTestHelper.test_sort(HeapSort, test_lists)
