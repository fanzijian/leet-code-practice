#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/jump-game-ii/


Authors: fanzijian
Date:    2020-05-05 23:50:56

"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N < 2:
            return 0
        dp = [0 for i in range(N)]
        max_idx = 0
        max_len = 0
        for i in xrange(0, N, 1):
            cur_len = i + nums[i]
            if cur_len > max_len:
                for j in xrange(max_len + 1, cur_len + 1, 1):
                    if j > N - 1:
                        break
                    dp[j] = dp[i] + 1
                max_idx = i
                max_len = i + nums[i]
        return dp[-1]
