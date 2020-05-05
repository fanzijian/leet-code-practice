#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/validate-binary-search-tree/


Authors: fanzijian
Date:    2020-05-05 23:50:56

"""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        rst = []
        def searchBST(root):
            if not root:
                return
            if root.left:
                searchBST(root.left)
            rst.append(root.val)
            if root.right:
                searchBST(root.right)
        searchBST(root)
        if not rst:
            return True
        pre = rst[0]
        for i in xrange(1, len(rst), 1):
            if rst[i] <= pre:
                return False
            pre = rst[i]
        return True
