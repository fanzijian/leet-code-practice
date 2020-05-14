#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题：https://leetcode-cn.com/problems/continuous-subarray-sum/

Authors: fanzijian
Date:    2020-05-12 16:46:56

"""
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        N = len(nums)
        total = 0
        S = [0]
        for num in nums:
            total += num
            S.append(total)
        # print S
        for i in xrange(0, N-1, 1):
            for j in xrange(i+2, N+1, 1):
                tmp = S[j] - S[i]
                if k == 0 and tmp == 0:
                    return True
                elif k != 0 and tmp % k == 0:
                    return True
        return False

    def checkSubarraySum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        N = len(nums)
        total_map = {0: -1}
        total = 0
        for i in xrange(0, N, 1):
            total += nums[i]
            if k != 0:
                total %= k
            if total in total_map:
                if i - total_map[total] > 1:
                    return True
            else:
                total_map[total] = i
        return False
