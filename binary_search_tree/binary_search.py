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


def binary_search2(lists, target, *args):
    if len(args):
        l = args[0]
        r = args[1]
        mid = l + (r - l) // 2
        if lists[mid] == target:
            return mid
        elif lists[mid] < target:
            return binary_search2(lists, target, mid + 1, r)
        else:
            return binary_search2(lists, target, l, mid - 1)
    else:
        return binary_search2(lists, target, 0, len(lists) - 1)


if __name__ == '__main__':
    test_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(test_lists, 6))
    print(binary_search2(test_lists, 8))
