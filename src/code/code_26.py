#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        n = 0
        for i in range(len(nums)):
            if nums[n] != nums[i]:
                n += 1
                nums[n] = nums[i]
        return n + 1

obj = Solution()
print obj.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
