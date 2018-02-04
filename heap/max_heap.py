#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 03/02/2018 3:49 PM
# @Author  : Lee
# @File    : max_heap.py
# @Software: PyCharm

import random


class MaxHeap(object):
    """
    构造函数中包含两种构造方式
    第一种为生成指定大小的空堆
    第二种则通过heapify进行建堆，时间复杂度为O(n)
    所创建最大堆均从索引1开始入堆计算，索引0位置默认为-1，不参与堆运算
    """

    def __init__(self, arg):
        """

        :param arg: 传入参数可能为capacity或者list
        若传入为capacity，则创建相应大小的空堆
        若传入为list, 则通过heapify进行建堆
        """
        if isinstance(arg, int):
            self.capacity = arg
            self.data = [-1]
            self.count = 0
        else:
            # heapify过程
            length = len(arg)
            self.data = [-1]
            self.capacity = length
            self.count = length
            for i in range(length):
                self.data.append(arg[i])
            # 此处最后一次shift_down操作在索引1处执行
            for k in range(self.count // 2, 0, -1):
                self._shift_down(k)

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def insert(self, item):
        assert self.count + 1 <= self.capacity
        self.data.append(item)
        self.count += 1
        self._shift_up(self.count)

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def extract_max(self):
        assert self.count > 0
        result = self.data[1]
        self._swap(1, self.count)
        self.count -= 1
        self._shift_down(1)
        return result

    def get_max(self):
        assert self.count > 0
        return self.data[1]

    """
    以下为核心辅助函数
    """

    def _shift_up(self, k):
        """
        此函数中 // 符号代表整除，结果为整数
        :param k: 节点位置
        """
        while (1 < k <= self.count) and self.data[k] > self.data[k // 2]:
            self._swap(k, k // 2)
            k //= 2

    def _shift_down(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            # 判断右子树是否存在并对左右子节点进行比较
            if j + 1 <= self.count and self.data[j] < self.data[j + 1]:
                j += 1
            if self.data[k] < self.data[j]:
                self._swap(k, j)
                k = j
            else:
                break


if __name__ == '__main__':
    max_heap = MaxHeap(10)
    for i in range(10):
        max_heap.insert(int(random.random() * 10))
    print(max_heap.data)

    max_heap2 = MaxHeap([10, 9, 8, 7, 1, 4, 50, 20, 30])
    print(max_heap2.data)
