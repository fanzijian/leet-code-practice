#!/usr/bin/env python
#-*- coding: utf-8 -*-


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if len(prices) <= 0:
            return 0
        min_prices = prices[0]

        for i in xrange(0, len(prices), 1):
            max_profit = max(max_profit, prices[i] - min_prices)
            if min_prices > prices[i]:
                min_prices = prices[i]

        return max_profit

obj = Solution()
print obj.maxProfit([7, 6, 4, 3, 1])
