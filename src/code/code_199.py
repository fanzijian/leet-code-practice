#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题：https://leetcode-cn.com/problems/binary-tree-right-side-view/
层序遍历，记录每层最后一个节点的值

Authors: fanzijian
Date:    2020-04-22 00:46:56

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        view = []
        while queue:
            level_queue = queue[:]
            view.append(level_queue[-1].val)
            queue = []
            for i in xrange(0, len(level_queue), 1):
                node = level_queue[i]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return view
