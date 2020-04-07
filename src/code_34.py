#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Solution(object):


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def get_extrame_index(nums, target, left=False):
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > target or (left and nums[mid] == target):
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        left_index = get_extrame_index(nums, target, True)
        if left_index >= len(nums) or nums[left_index] != target:
            return [-1, -1]
        return [left_index, get_extrame_index(nums, target, False) - 1]

obj = Solution()
print obj.searchRange([1,2,2,5], 2)