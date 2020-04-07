#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 基础递归解法
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rst = []
        if root == None:
            return rst
        if root.left != None:
            rst.extend(self.inorderTraversal(root.left))
        rst.append(root.val)
        if root.right != None:
            rst.extend(self.inorderTraversal(root.right))
        return rst
'''
# 迭代解法
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        p_list = [root]
        rst = []
        if root == None:
            return rst
        while p_list:
            # 右子树存储
            root = p_list.pop()
            if isinstance(root, int):
                rst.append(root)
                continue
            if root.right is not None:
                p_list.append(root.right)
            p_list.append(root.val)
            if root.left is not None:
                p_list.append(root.left)
        return rst


root = TreeNode(1)
# root.left = TreeNode()
root.right = TreeNode(2)
root.right.left = TreeNode(3)
obj = Solution()
print obj.inorderTraversal(root)
