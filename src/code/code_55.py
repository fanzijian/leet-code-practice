#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题: https://leetcode-cn.com/problems/jump-game/

维护最远距离K，遍历数组，如果当前的i+nums[i] > K,说明可以达到更远位置，
如果 K < i,那么说明，中间有不可达的地方

Authors: fanzijian
Date:    2020-04-17 23:50:56

"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        k = 0
        N = len(nums)
        for i in xrange(0, N, 1):
            if k < i:
                return False
            k = max(k, i + nums[i])
            if k >= N - 1:
                return True
        return True

nums = [1, 1, 0]
obj = Solution()
print obj.canJump(nums)
