#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pt_list = [[p],[q]]
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        while pt_list[0]:
            p = pt_list[0].pop()
            q = pt_list[1].pop()
            if isinstance(p, int) != isinstance(q, int):
                print 'type'
                return False

            if isinstance(p, int) and isinstance(q, int):
                # 节点不相等
                if p != q:
                    print p, q, 1
                    return False
                continue

            if isinstance(p.left, TreeNode) == isinstance(q.left, TreeNode):
                if p.left is not None:
                    pt_list[0].append(p.left)
                    pt_list[1].append(q.left)
            else:
                return False
            pt_list[0].append(p.val)
            pt_list[1].append(q.val)
            if isinstance(p.right, TreeNode) == isinstance(q.right, TreeNode):
                if p.right is not None:
                    pt_list[0].append(p.right)
                    pt_list[1].append(q.right)
            else:
                print p.val, q.val, 3
                return False
        return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(1)
root2 = TreeNode(1)
root2.left = TreeNode(1)
root2.right = TreeNode(2)
obj = Solution()
print obj.isSameTree(root, root2)
