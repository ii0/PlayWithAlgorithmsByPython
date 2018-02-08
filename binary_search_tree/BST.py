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

    def insert(self, *args):
        """
        像以node为根节点的二分搜索树中，插入节点(key, value)
        :param args: Node, Key, Value
        :return: 插入节点后的新bst
        """
        if len(args) == 2:
            key, value = args
            self.insert(self.root, key, value)
        else:
            node, key, value = args
            if node is None:
                self.count += 1
                return Node(key, value)

            if key == node.key:
                node.value = value
            elif key < node.key:
                node.left = self.insert(node.left, key, value)
            else:
                # key > node.key
                node.right = self.insert(node.right, key, value)
        return node




class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None


