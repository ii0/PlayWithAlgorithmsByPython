#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 15:58
# @Author  : Lee
# @File    : selection_sort.py
# @Software: PyCharm

from utils.common import swap

def selection_sort(lists):
    length = len(lists)

    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if lists[min_index] > lists[j]:
                min_index = j
        swap(lists, min_index, i)
    return lists

if __name__ == '__main__':
    lists = [10, 8, 9, 7, 5, 3, 2, 1, 100]
    print(selection_sort(lists))