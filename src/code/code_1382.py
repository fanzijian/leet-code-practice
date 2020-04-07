#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        node_list = []
        def midSearch(cur):
            if cur.left:
                midSearch(cur.left)
            node_list.append(cur)
            if cur.right:
                midSearch(cur.right)
        midSearch(root)
        N = len(node_list)
        def rebuildFullBST(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            cur = node_list[mid]
            cur.left = rebuildFullBST(l, mid - 1)
            cur.right = rebuildFullBST(mid + 1, r)
            return cur

        return rebuildFullBST(0, N-1)
