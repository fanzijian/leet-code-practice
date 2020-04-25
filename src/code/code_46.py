#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/permutations/

Authors: fanzijian
Date:    2020-04-26 16:01:56

"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums]
        rst = []
        for n in nums:
            tmp = nums[:]
            tmp.remove(n)
            for i in self.permute(tmp):
                rst.append([n] + i)
        return rst
