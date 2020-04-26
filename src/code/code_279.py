#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题: https://leetcode-cn.com/problems/perfect-squares/

Authors: fanzijian
Date:    2020-04-26 23:35:56
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n for i in xrange(0, n+1, 1)]
        dp[0] = 0
        for i in xrange(1, n+1, 1):
            j = 1
            while j ** 2 < i:
                idx = j ** 2
                if dp[i-idx] + 1 < dp[i]:
                    dp[i] = dp[i-idx] + 1
                j += 1
            if j ** 2 == i:
                dp[i] = 1
        return dp[-1]

obj = Solution()

print obj.numSquares(1)
