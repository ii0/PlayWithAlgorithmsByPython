#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 07/02/2018 6:21 PM
# @Author  : Lee
# @File    : binary_search.py
# @Software: PyCharm


def binary_search(lists, target):
    l = 0
    r = len(lists) - 1
    while l <= r:
        mid = l + (r - l) // 2

        if lists[mid] == target:
            return mid
        elif lists[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


if __name__ == '__main__':
    test_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(test_lists, 6))
