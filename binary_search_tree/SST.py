#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/02/2018 5:06 PM
# @Author  : Lee
# @File    : SST.py
# @Software: PyCharm


class SST(object):

    def __init__(self, head=None, count=0):
        self.head = head
        self.count = count

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def insert(self, key, value):
        """
        查找顺序表，看是否存在同样大小的key
        若存在，则更新value值
        若不存在，则创建新节点，插入表头前面
        :param key:
        :param value:
        :return:
        """
        node = self.head
        while node is not None:
            if key == node.key:
                node.value = value
                return
            node = node.next
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def contain(self, key):
        node = self.head
        while node is not None:
            if key == node.key:
                return True
            node = node.next
        return False

    def search(self, key):
        """
        查找链表中key所对应的value
        :param key:
        :return:
        """
        node = self.head
        while node is not None:
            if key == node.key:
                return node.value
            node = node.next
        return None

    def remove(self, key):
        """
        首先考虑链表是否为空
        其次要删除的节点是否为头节点

        :param key:
        :return:
        """
        if self.head is None:
            return

        if key == self.head.key:
            del_head = self.head
            self.head = self.head.next
            del_head.next = None
            self.count -= 1
            return

        node = self.head
        while node.next is not None and node.next.key != key:
            node = node.next

        if node.next is None:
            del_node = node.next
            node.next = del_node.next
            del_node.next = None
            self.count -= 1
            return


class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

