#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/three-steps-problem-lcci/

动态规划

Authors: fanzijian
Date:    2020-05-19 23:33:56

"""
class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 2, 4]
        if n <= 3:
            return dp[n-1]
        cur = 0
        for i in xrange(3, n, 1):
            dp.append(sum(dp[-3:]) % 1000000007)
        return dp[-1]