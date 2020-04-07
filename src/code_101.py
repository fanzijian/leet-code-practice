#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pt = [root, root]
        while pt:
            t1 = pt.pop()
            t2 = pt.pop()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            pt.extend([t1.left, t2.right])
            pt.extend([t1.right, t2.left])
        return True
