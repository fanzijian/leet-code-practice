#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # 目标值在[mid, right]
                left = mid + 1
            else:
                # 目标值在[left, mid]
                right = mid - 1
        return left

obj = Solution()
print obj.searchInsert([1,2], 3)
