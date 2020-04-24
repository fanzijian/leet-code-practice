#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/subarray-sum-equals-k/

O(N)
利用hash表存储累计和，如果存在sum(i, j) == k
那么则有 sum[0, j] - sum[0, i] == k
即 sum[0, i]在该hash表中的次数，即对应和j可以组成的连续和为k的次数

O(N^2)
遍历并计算连续累计和即可

Authors: fanzijian
Date:    2020-04-12 11:23:56

"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        sum_map = {0: 1}
        total = 0
        count = 0
        for i in xrange(0, N, 1):
            total += nums[i]
            if (total - k) in sum_map:
                count += sum_map[total - k]
            if total not in sum_map:
                sum_map[total] = 0
            sum_map[total] += 1
        return count