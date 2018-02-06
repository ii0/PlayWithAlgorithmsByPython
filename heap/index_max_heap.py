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

    def __init__(self, lists):
        length = len(lists)
        self.data = [-1]
        self.index = [-1]
        self.capacity = length
        self.count = length

        for i in range(length):
            self.data.append(lists[i])
            self.index.append(i+1)
        # 此处最后一次shift_down操作在索引1处执行
        for k in range(self.count // 2, 0, -1):
            self._shift_down(k)

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def insert(self, i, item):
        """

        :param i: 索引值
        :param item: 数据值
        :return:
        """
        assert self.count + 1 <= self.capacity
        assert i >= 0 and i + 1 <= self.capacity
        self.data.append(item)
        self.count += 1
        self.index.append(i)
        self._shift_up(self.count)

    def _swap_index(self, i, j):
        self.index[i], self.index[j] = self.index[j], self.index[i]

    def extract_max_index(self):
        assert self.count > 0
        result = self.index[1] - 1
        self._swap_index(1, self.count)
        self.count -= 1
        self._shift_down(1)
        return result

    def extract_max(self):
        assert self.count > 0
        result = self.data[self.index[1]]
        self._swap_index(1, self.count)
        self.count -= 1
        self._shift_down(1)
        return result

    def get_max_index(self):
        assert self.count > 0
        return self.index[1] - 1

    def get_max(self):
        assert self.count > 0
        return self.data[self.index[1]]

    def change(self, i, item):
        i += 1
        self.data[i] = item
        for j in range(self.count):
            if self.index[j] == i:
                self._shift_up(j)
                self._shift_down(j)
                return

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
    test_lists = [10, 9, 8, 7, 1, 4, 5, 2, 3, 6]
    index_max_heap = IndexMaxHeap(test_lists)
    print(index_max_heap.index)
    print(index_max_heap.data)
