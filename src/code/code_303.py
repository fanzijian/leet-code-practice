#!/usr/bin/env python
#-*- coding: utf-8 -*-

dp = []


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for i in xrange(0, len(nums), 1):
            tmp = [0 for k in nums]
            for j in xrange(i, len(nums), 1):
                if i == j:
                    tmp[j] = nums[j]
                else:
                    tmp[j] = tmp[j-1] + nums[j]
            dp.append(tmp)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if len(dp) == 0:
            return 0
        return dp[i][j]


# Your NumArray object will be instantiated and called as such:
# ["NumArray","sumRange","sumRange","sumRange"]
# [[], [0, 2], [2, 5], [0, 5]]
#["NumArray","sumRange"] [[[-1]], [0, 0]]
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0, 2)
param_2 = obj.sumRange(2,5)
print param_2
