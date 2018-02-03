#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 03/02/2018 3:49 PM
# @Author  : Lee
# @File    : max_heap.py
# @Software: PyCharm

import random


class MaxHeap(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [-1] * (capacity + 1)
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def insert(self, item):
        assert self.count + 1 <= self.capacity
        self.data[self.count + 1] = item
        self.count += 1
        self.shift_up(self.count)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    """
    以下为核心辅助函数
    """

    def shift_up(self, k):
        """
        此函数中 // 符号代表整除，结果为整数
        :param k: 节点位置
        :return:
        """
        while k <= self.count and self.data[k] > self.data[k//2]:
            self.swap(k, k//2)
            k //= 2


if __name__ == '__main__':
    max_heap = MaxHeap(100)
    print(max_heap.size())
    for i in range(50):
        max_heap.insert(int(random.random() * 100))
    print(max_heap.size())


