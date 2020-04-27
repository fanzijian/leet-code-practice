#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

方法一: O(n^2)遍历两边，记录每个位置的最大值情况，然后对比如果用到第N次价格卖出的情况


Authors: fanzijian
Date:    2020-04-27 16:33:56

"""
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [0 for i in xrange(0, len(prices), 1)]
        for i in xrange(1, len(prices), 1):
            max_total = dp[i-1]
            for j in xrange(0, i, 1):
                if j >= 2:
                    max_total = max(prices[i] - prices[j] + dp[j-2], max_total)
                else:
                    max_total = max(prices[i] - prices[j], max_total)
            dp[i] = max_total
        return dp[-1]

    def maxProfit2(self, prices):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = -sys.maxint
        dp_pre_0 = 0
        for i in xrange(0, n, 1):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = tmp
        return dp_i_0

