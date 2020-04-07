#!/usr/bin/env python
#-*- coding: utf-8 -*-


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cur_max = nums[0]
        max_max = nums[0]
        for i in xrange(1, n, 1):
            cur_max = max(nums[i], cur_max + nums[i])
            max_max = max(cur_max, max_max)
        return max_max

obj = Solution()
print obj.maxSubArray([-2, -1, 4])
