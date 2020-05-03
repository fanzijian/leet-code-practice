#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
?????https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/submissions/

Authors: fanzijian
Date:    2020-05-03 11:23:56

"""
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        if not nums:
            return 0
        count_range = [0, 0]
        max_idx = 0
        min_idx = 0
        N = len(nums)
        max_len = 0
        idx = 0
        while idx < N:
            # update max_idx,min_idx
            if nums[idx] >= nums[max_idx]:
                max_idx = idx
            if nums[idx] <= nums[min_idx]:
                min_idx = idx
            if nums[max_idx] - nums[min_idx] <= limit:
                count_range[1] = idx
                idx += 1
                max_len = max(count_range[1] - count_range[0] + 1, max_len)
            else:
                idx = min(min_idx, max_idx)
                idx += 1
                min_idx = idx
                max_idx = idx
                count_range = [idx, idx]
        return max_len


nums = [24, 12, 71, 33, 5, 87, 10, 11, 3, 58,
         2, 97, 97, 36, 32, 35, 15, 80, 24, 45,
        38, 9, 22, 21, 33, 68, 22, 85, 35, 83,
        92, 38, 59, 90, 42, 64, 61, 15, 4, 40,
        50, 44, 54, 25, 34, 14, 33, 94, 66, 27,
        78, 56, 3, 29, 3, 51, 19, 5, 93, 21,
        58, 91, 65, 87, 55, 70, 29, 81, 89, 67,
        58, 29, 68, 84, 4, 51, 87, 74, 42, 85,
        81, 55, 8, 95, 39]
limit = 87
obj = Solution()
print obj.longestSubarray(nums, limit)
