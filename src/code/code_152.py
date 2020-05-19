#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/maximum-product-subarray/

考虑动态规划解决

Authors: fanzijian
Date:    2020-05-18 23:33:56

"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = nums[0]
        min_num = nums[0]
        pre_max = [1, 0]
        pre_min = [1, 0]
        for num in nums:
            if num == 0:
                pre_max = [0, 0]
                pre_min = [0, 0]
            else:
                tmp_pre_min = num * pre_min[0]
                tmp_pre_max = num * pre_max[0]
                if pre_min[1] == 0:
                    pre_min = [num, 1]
                else:
                    pre_min[0] = min(tmp_pre_max, tmp_pre_min, num)
                if pre_max[1] == 0:
                    pre_max = [num, 1]
                else:
                    if tmp_pre_max < pre_max[0]:
                        pre_max[1] = 0
                    else:
                        pre_max[1] = 1
                pre_max[0] = max(tmp_pre_max, tmp_pre_min, num)
            # print pre_max, pre_min,tmp_pre_max,tmp_pre_min
            if pre_max[0] > max_num:
                max_num = pre_max[0]
        return max_num