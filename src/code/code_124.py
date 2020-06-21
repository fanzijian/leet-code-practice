#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/submissions/

后续遍历

Authors: fanzijian
Date:    2020-06-21 23:33:56

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        maxSum = [root.val]
        def DFS(root):
            tmp = [0]
            if root.left:
                tmp.append(DFS(root.left))
            if root.right:
                tmp.append(DFS(root.right))

            max_val = max(tmp)
            maxSum[0] = max(root.val, root.val + max_val, sum(tmp) + root.val, maxSum[0])
            if max_val < 0:
                return root.val
            else:
                return root.val + max_val
        DFS(root)
        return maxSum[0]


