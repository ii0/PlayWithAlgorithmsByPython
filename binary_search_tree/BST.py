#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 08/02/2018 12:21 AM
# @Author  : Lee
# @File    : BST.py
# @Software: PyCharm

from utils.sort_test_helper import SortTestHelper

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
            self.root = self.insert(self.root, key, value)
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

    def contain(self, *args):
        """
        查找BST中是否包含键key所对应的值
        :param args: node, key
        :return: true, false
        """
        if len(args) == 2:
            node, key = args
            if node is None:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return self.contain(node.left, key)
            else:
                return self.contain(node.right, key)
        else:
            key = args[0]
            self.contain(self.root, key)

    def search(self, *args):
        """
        查找以node为根的BST中查找key所对应value
        :param args: node, key
        :return: value
        """
        if len(args) == 2:
            node, key = args
            if node is None:
                return None
            if key == node.key:
                return node.value
            elif key < node.key:
                return self.search(node.left, key)
            else:
                return self.search(node.right, key)
        else:
            key = args[0]
            return self.search(self.root, key)


class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None


if __name__ == '__main__':
    test_array = SortTestHelper.generate_near_ordered_list(6, 6)
    bst = BST()
    for i in range(len(test_array)):
        bst.insert(i, test_array[i])