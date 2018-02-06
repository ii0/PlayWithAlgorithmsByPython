#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 06/02/2018 9:32 PM
# @Author  : Lee
# @File    : index_max_heap.py
# @Software: PyCharm

import random


class IndexMaxHeap(object):
    """
    索引最大堆
    """

    def __init__(self, capacity):
        self.data = [-1]
        self.index = [-1]
        self.reverse = [-1] * (capacity+1)
        self.capacity = capacity
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def insert(self, i, item):
        """
        插入的索引值从0开始计数，需要先内部+1
        :param i: 索引值
        :param item: 数据值
        :return:
        """
        assert self.count + 1 <= self.capacity
        assert i >= 0 and i + 1 <= self.capacity
        i += 1
        self.data.append(item)
        self.count += 1
        self.index.append(i)
        self.reverse[i] = self.count
        self._shift_up(self.count)

    def _swap_index(self, i, j):
        self.index[i], self.index[j] = self.index[j], self.index[i]
        self.reverse[self.index[i]] = i
        self.reverse[self.index[j]] = j

    def extract_max_index(self):
        assert self.count > 0
        result = self.index[1] - 1
        self._swap_index(1, self.count)
        self.reverse[self.index[self.count]] = -1
        self.count -= 1
        self._shift_down(1)
        return result

    def extract_max(self):
        assert self.count > 0
        result = self.data[self.index[1]]
        self._swap_index(1, self.count)
        self.reverse[self.index[self.count]] = -1
        self.count -= 1
        self._shift_down(1)
        return result

    def get_max_index(self):
        assert self.count > 0
        return self.index[1] - 1

    def get_max(self):
        assert self.count > 0
        return self.data[self.index[1]]

    def _contain(self, i):
        assert i >= 0 and i + 1 <= self.capacity
        return self.reverse[i] != -1

    def change(self, i, item):
        """
        索引值从0开始计数，需要先内部+1
        :param i: 索引值
        :param item:
        :return:
        """
        assert self._contain(i)
        i += 1
        self.data[i] = item
        # for j in range(self.count):
        #     if self.index[j] == i:
        #         self._shift_up(j)
        #         self._shift_down(j)
        #         return
        self._shift_up(self.reverse[i])
        self._shift_down(self.reverse[i])

    """
    以下为核心辅助函数
    """

    def _shift_up(self, k):
        """
        此函数中 // 符号代表整除，结果为整数
        :param k: 节点位置
        """
        while (1 < k <= self.count) and self.data[self.index[k]] > self.data[self.index[k // 2]]:
            self._swap_index(k, k // 2)
            k //= 2

    def _shift_down(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            # 判断右子树是否存在并对左右子节点进行比较
            if j + 1 <= self.count and self.data[self.index[j]] < self.data[self.index[j + 1]]:
                j += 1
            if self.data[self.index[k]] < self.data[self.index[j]]:
                self._swap_index(k, j)
                k = j
            else:
                break


if __name__ == '__main__':
    """
    测试结果：
             
    堆中索引值->index:  [-1, 10, 9, 6, 7, 8, 2, 5, 1, 4, 3]
    堆中数据值->data:   [-1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    反向查找->reverse:  [-1, 8, 6, 10, 9, 7, 3, 4, 5, 2, 1]
    
    验证方式：
    index[x] = y
    reverse[y] = x
    通过index堆得结构，将data数据填入，构成最大堆
    """
    index_max_heap = IndexMaxHeap(10)
    for i in range(10):
        index_max_heap.insert(i, 2*i + 1)
    print(index_max_heap.index)
    print(index_max_heap.data)
    print(index_max_heap.reverse)
