#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)
        sum_closest = sys.maxint
        for i in xrange(0, length, 1):
            m = i - 1
            n = i + 1
            if m < 0 or n >= length:
                continue
            while True:
                if m < 0 or n >= length:
                    break

                tmp = nums[m] + nums[n] + nums[i] - target
                if abs(sum_closest - target) > abs(tmp):
                    sum_closest = nums[m] + nums[n] + nums[i]
                if tmp > 0:
                    m -= 1
                elif tmp < 0:
                    n += 1
                else:
                    return nums[m] + nums[n] + nums[i]
        return sum_closest

obj = Solution()
print obj.threeSumClosest([1, 1, 1, 0], 100)
