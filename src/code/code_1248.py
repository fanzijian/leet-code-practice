#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题：https://leetcode-cn.com/problems/count-number-of-nice-subarrays/

Authors: fanzijian
Date:    2020-04-21 20:46:56

"""
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 记录奇数下标
        one_list = [i for i in xrange(0, len(nums), 1) if nums[i] % 2 == 1]
        N = len(one_list)
        if N < k:
            return 0
        cnt = 0
        # 遍历计算总数，左边偶数量+1 * 右边偶数量+1
        for e_idx in xrange(k-1, N, 1):
            s_idx = e_idx - k + 1
            pre_interval = one_list[s_idx] - one_list[s_idx-1] if s_idx > 0 else (one_list[0] + 1)
            next_interval = one_list[e_idx+1] - one_list[e_idx] if e_idx < N - 1 else (len(nums) - one_list[-1])
            cnt += pre_interval * next_interval
        return cnt
