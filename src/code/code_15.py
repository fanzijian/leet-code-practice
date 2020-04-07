#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        todo: 理解错题目意思，导致改写的解法非最优
        """
        nums = sorted(nums)
        length = len(nums)
        result = set()
        for i in xrange(0, length, 1):
            m = 0
            n = length - 1
            while True:
                if m >= i or n <= i:
                    break
                total = nums[m] + nums[n] + nums[i]
                if total == 0:
                    tmp = "%s,%s,%s" % (nums[i], nums[m], nums[n])
                    result.add(tmp)
                    while True:
                        if m >= i or n <= i:
                            break
                        if nums[n] == nums[n-1]:
                            n -= 1
                            continue
                        elif nums[m] == nums[m+1]:
                            m += 1
                            continue
                        else:
                            m += 1
                            break
                elif total > 0:
                    n -= 1
                elif total < 0:
                    m += 1
        return [[int(c) for c in d.split(',')] for d in result]

obj = Solution()
print obj.threeSum([0, 0, 0, 0])
