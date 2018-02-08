#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 08/02/2018 12:21 AM
# @Author  : Lee
# @File    : BST.py
# @Software: PyCharm


class BST(object):

    def __init__(self, root=None, count=0):
        self.root = root
        self.count = count

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0


class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None


