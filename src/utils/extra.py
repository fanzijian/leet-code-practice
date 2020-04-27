#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
出入一个非负数组，数字代表跳的步长，求最小达到末尾的次数

Authors: fanzijian
Date:    2020-04-27 16:33:56

"""

class Solution(object):
    def maxStep(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        N = len(nums)
        next_queue = set([0])
        step = 0
        is_visited = set()
        while next_queue:
            queue = next_queue.copy()
            next_queue = set()
            step += 1
            while queue:
                idx = queue.pop()
                if idx + nums[idx] >= N:
                    return step
                if idx not in is_visited:
                    is_visited.add(idx)
                    for i in xrange(0, nums[idx], 1):
                        if idx + i + 1 not in is_visited:
                            next_queue.add(idx + i + 1)
        return -1
nums = [1,2,3,0,12,4,9,10]
obj = Solution()
print obj.maxStep(nums)
