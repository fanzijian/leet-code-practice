#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

一行一行处理，前K名一定是每次处理之后的前K名产生的！

Authors: fanzijian
Date:    2020-05-03 11:23:56

"""
class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        pre = []
        for row in mat:
            if not pre:
                for x in row:
                    pre.append(x)
            else:
                cur = []
                for x in row:
                    for y in pre:
                        cur.append(x+y)
                pre = sorted(cur)
            if len(pre)>k:
                pre = pre[0:k]
        return pre[-1]
