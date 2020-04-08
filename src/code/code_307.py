#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/range-sum-query-mutable/

Authors: fanzijian(fanzijian@baidu.com)
Date:    2020-04-08 11:23:56

"""
class NumArray(object):
    def __init__(self, nums):
        """
        Arguments:
            nums {[list]} -- [数组]
        """
        total = 0
        for i in xrange(0, len(nums), 1):
            total += nums[i]
            nums[i] = total
        self.nums = nums

    def update(self, i, val):
        """[更新序号为i的元素值为val]

        Arguments:
            i {[int]} -- [序号]
            val {[int]} -- [数值]
        """
        delta = self.nums[i] - (self.nums[i-1] if i > 0 else 0) - val
        for m in xrange(i, len(self.nums), 1):
            self.nums[m] -= delta

    def sumRange(self, i, j):
        """[返回序号i到序号j的元素总和，i<=j]

        Arguments:
            i {[int]} -- [数组序号]
            j {[int]} -- [数组序号]
        """
        max_total = self.nums[j]
        min_total = self.nums[i-1] if i > 0 else 0
        return max_total - min_total
