#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
二叉查找树

Authors: fanzijian
Date:    2020-05-12 16:46:56

"""
class Node(object):
    def __init__(self, val, father):
        self.val = val
        self.left = None
        self.right = None
        self.father = None


class BST(object):
    def __init__(self, nums):
        self.root = Node(-1)
        pre = self.root
        for num in nums:
            self.add(num)

    def search(self, num):
        cur = self.root.right
        pre = self.root
        while cur:
            if cur.val == num:
                return True, cur
            if cur.val > num:
                pre = cur
                cur = cur.left
            else:
                pre = cur
                cur = cur.right
        return False, pre

    def add(self, num):
        flag, pre = self.search(num)
        if not flag:
            if pre.val > num:
                pre.left = Node(num, pre)
            else:
                pre.right = Node(num, right)

    def search_max_left(self, cur):
        while cur and cur.right:
            cur = cur.right
        return cur

    def search_min_right(self, cur):
        while cur and cur.left:
            cur = cur.left
        return cur

    def delete(self, num):
        flag, cur = self.search(num)
        if not flag:
            return False
        fa = cur.father
        if not cur.left and not cur.right:
            if fa.left == cur:
                fa.left = None
            else:
                fa.right = None

        if cur.left:
            max_left = self.search_max_left(cur.left)
            max_left.father.right = max_left.left
            max_left.left = cur.left
            max_left.right = cur.right
            if fa.left == cur:
                fa.left = max_left
            else:
                fa.right = max_left
        elif cur.right:
            min_right = self.search_min_right(cur.right)
            min_right.father.left = min_right.right
            min_right.right = cur.right
            min_right.left = cur.left
            if fa.left == cur:
                fa.left = min_right
            else:
                fa.right = min_right

    def BFS(self):
        pass

    def DFS(self):
        pass
