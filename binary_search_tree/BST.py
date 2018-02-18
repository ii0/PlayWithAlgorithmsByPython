#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 08/02/2018 12:21 AM
# @Author  : Lee
# @File    : BST.py
# @Software: PyCharm

import queue

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

    """
    深度优先遍历：前、中、后序遍历，采用递归方式
    """
    def pre_order(self):
        self._pre_order(self.root)

    def in_order(self):
        self._in_order(self.root)

    def post_order(self):
        self._post_order(self.root)

    def _pre_order(self, root):
        if root is not None:
            print(root.key)
            self._pre_order(root.left)
            self._pre_order(root.right)

    def _in_order(self, root):
        if root is not None:
            self._in_order(root.left)
            print(root.key)
            self._in_order(root.right)

    def _post_order(self, root):
        if root is not None:
            self._post_order(root.left)
            self._post_order(root.right)
            print(root.key)

    def level_order(self):
        """
        广度优先遍历
        :return:
        """
        q = queue.Queue()
        q.put(self.root)
        while not q.empty():
            node = q.get()
            print(node.key)

            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)

    def _minimum(self, node):
        """

        :param node:
        :return:返回以node为根的BST的最小键值所在的节点
        """
        if node.left is None:
            return node
        return self._minimum(node.left)

    def _maximum(self, node):
        """

        :param node:
        :return:返回以node为根的BST的最大键值所在的节点
        """
        if node.right is None:
            return node
        return self._maximum(node.right)

    def _remove_max(self, node):
        """
        删除最大节点
        :param node:
        :return:
        """
        if node.right is None:
            left_node = node.left
            node.left = None
            self.count -= 1
            return left_node
        node.right = self._remove_max(node.right)
        return node

    def _remove_min(self, node):
        """
        删除最小节点
        :param node:
        :return:
        """
        if node.left is None:
            right_node = node.right
            node.right = None
            self.count -= 1
            return right_node
        node.left = self._remove_min(node.left)
        return node

    def minimum(self):
        assert self.count != 0
        min_node = self._minimum(self.root)
        return min_node

    def maximum(self):
        assert self.count != 0
        max_node = self._maximum(self.root)
        return max_node

    def remove_max(self):
        if self.root is not None:
            self.root = self._remove_max(self.root)

    def remove_min(self):
        if self.root is not None:
            self.root = self._remove_min(self.root)


class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None


if __name__ == '__main__':
    test_array = SortTestHelper.generate_random_list(6, 0, 50)
    # print(test_array)
    bst = BST()
    for i in range(len(test_array)):
        bst.insert(test_array[i], test_array[i])
    # bst.pre_order()
    bst.level_order()
    # bst.in_order()
    # bst.post_order()