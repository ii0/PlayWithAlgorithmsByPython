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
        self.data = [-1]
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def insert(self, item):
        assert self.count + 1 <= self.capacity
        self.data.append(item)
        self.count += 1
        self.shift_up(self.count)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def extract_max(self):
        assert self.count > 0
        result = self.data[1]
        self.swap(1, self.count)
        self.count -= 1
        self.shift_down(1)
        return result

    def get_max(self):
        assert self.count > 0
        return self.data[1]

    """
    以下为核心辅助函数
    """

    def shift_up(self, k):
        """
        此函数中 // 符号代表整除，结果为整数
        :param k: 节点位置
        """
        while (1 < k <= self.count) and self.data[k] > self.data[k//2]:
            self.swap(k, k//2)
            k //= 2

    def shift_down(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            # 判断右子树是否存在并对左右子节点进行比较
            if j + 1 <= self.count and self.data[j] < self.data[j+1]:
                j += 1
            if self.data[k] < self.data[j]:
                self.swap(k, j)
                k = j
            else:
                break


if __name__ == '__main__':
    max_heap = MaxHeap(10)
    for i in range(10):
        max_heap.insert(int(random.random() * 10))
    print(max_heap.data)
