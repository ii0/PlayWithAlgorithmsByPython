#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 04/02/2018 5:02 PM
# @Author  : Lee
# @File    : min_heap.py
# @Software: PyCharm

import random


class MinHeap(object):
    """
    原理与MaxHeap一致
    故不多做注释
    """
    def __init__(self, arg):
        if isinstance(arg, int):
            self.capacity = arg
            self.data = [-1]
            self.count = 0
        else:
            length = len(arg)
            self.capacity = length
            self.data = [-1]
            self.count = length
            for i in range(length):
                self.data.append(arg[i])
            for k in range(self.count // 2, 0, -1):
                self._shift_down(k)

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def insert(self, item):
        assert self.count + 1 <= self.capacity
        self.data.append(item)
        self.count += 1
        self._shift_up(self.count)

    def extract_min(self):
        assert self.count > 0
        result = self.data[1]
        self.swap(1, self.count)
        self.count -= 1
        self._shift_down(1)
        return result

    def get_min(self):
        return self.data[1]

    """
    以下为核心辅助函数
    """

    def _shift_up(self, k):
        """
        此函数中 // 符号代表整除，结果为整数
        :param k: 节点位置
        """
        while (1 < k <= self.count) and self.data[k] < self.data[k // 2]:
            self._swap(k, k // 2)
            k //= 2

    def _shift_down(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            # 判断右子树是否存在并对左右子节点进行比较
            if j + 1 <= self.count and self.data[j] > self.data[j + 1]:
                j += 1
            if self.data[k] > self.data[j]:
                self._swap(k, j)
                k = j
            else:
                break


if __name__ == '__main__':
    max_heap = MinHeap(10)
    for i in range(10):
        max_heap.insert(int(random.random() * 10))
    print(max_heap.data)

    max_heap2 = MinHeap([10, 9, 8, 7, 1, 4, 50, 20, 30])
    print(max_heap2.data)