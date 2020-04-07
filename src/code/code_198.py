#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [nums[0], max(nums[0:2])]
        for i in xrange(2, len(nums), 1):
            dp.append(max(dp[i-2] + nums[i], dp[i-1]))
        # print dp
        return dp[-1]

obj = Solution()
print obj.rob([2,7,0,0,9])
