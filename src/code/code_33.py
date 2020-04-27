#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

二分查找，二分之后，必定有一半是有序的，判断是否在有序的范围内，不在则表示可能在另外一半
Authors: fanzijian
Date:    2020-04-27 15:45:56

"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while True:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid
            if left > right:
                return -1
            if nums[mid] >= nums[left]:
                # 左边递增
                # 判断是否是在左边范围内
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # 右侧递增
                # 判断是否是在右边范围内
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
