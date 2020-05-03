#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

Authors: fanzijian
Date:    2020-05-03 11:23:56

"""
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pre = None
        for i in xrange(0, len(nums), 1):
            if nums[i] == 1 and pre:
                if i - pre > k:
                    continue
                else:
                    return False
            if nums[i] == 1 and not pre:
                pre = i
        return True
