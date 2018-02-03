#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 03/02/2018 3:49 PM
# @Author  : Lee
# @File    : max_heap.py
# @Software: PyCharm


class MaxHeap(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [-1] * (capacity + 1)
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count


if __name__ == '__main__':
    max_heap = MaxHeap(100)
    print(max_heap.size())

