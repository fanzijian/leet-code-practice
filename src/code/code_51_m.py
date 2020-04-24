#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/

Authors: fanzijian
Date:    2020-04-24 16:01:56

"""

class Solution(object):

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        N = len(nums)
        if N < 2:
            return 0
        mid = N // 2
        S1 = nums[:mid]
        S2 = nums[mid:]
        total += self.reversePairs(S1)
        total += self.reversePairs(S2)
        total += self.merge(S1, S2, nums)
        return total

    def merge(self, S1, S2, S):
        """[合并并记录S1和S2的总逆序数对，其中S1和S2是已经排序过的了
        利用双指针，快速计算]
        """
        len_1 = len(S1)
        len_2 = len(S2)
        cnt = i = j = 0

        while i < len_1 and j < len_2:
            if S1[i] > S2[j]:
                S[i+j] = S2[j]
                cnt += len_1 - i
                j += 1
            else:
                S[i+j] = S1[i]
                i += 1
        if i < len_1:
            S[i+j:] = S1[-len_1+i:]
        if j < len_2:
            S[i+j:] = S2[-len_2+j:]
        return cnt



obj = Solution()
print obj.reversePairs(
    [7, 5, 6, 4])
