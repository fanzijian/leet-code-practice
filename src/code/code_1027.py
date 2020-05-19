#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/longest-arithmetic-sequence/

动态规划

Authors: fanzijian
Date:    2020-05-19 23:33:56

"""
class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        dp = []
        max_len = 0
        for i in xrange(0, N, 1):
            dp.append({})
            for j in xrange(0, i, 1):
                delta = A[i] - A[j]
                if delta in dp[j]:
                    dp[i][delta] = dp[j][delta] + 1
                else:
                    dp[i][delta] = 2
                max_len = max(dp[i][delta], max_len)
        return max_len


