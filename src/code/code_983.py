#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/minimum-cost-for-tickets/submissions/

Authors: fanzijian
Date:    2020-05-06 23:50:56

"""
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        N = len(days)
        max_day = max(days)
        dp = [0 for i in xrange(0, max_day + 1, 1)]
        j = 1
        for i in xrange(0, N, 1):
            while j < days[i]:
                dp[j] = dp[j-1]
                j += 1
            tmp = [dp[j-1] + costs[0]]
            if j >= 7:
                tmp.append(dp[j-7] + costs[1])
            else:
                tmp.append(dp[0] + costs[1])
            if j >= 30:
                tmp.append(dp[j-30] + costs[2])
            else:
                tmp.append(dp[0] + costs[2])
            dp[j] = min(tmp)
            j += 1
        return dp[days[-1]]