#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/next-permutation/


Authors: fanzijian
Date:    2020-05-20 23:33:56

"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N <= 1:
            return nums
        pre = nums[N-1]
        y = N - 1
        x = -1
        for i in xrange(N-1, -1, -1):
            if nums[i] < pre:
                x = i + 1
                break
            else:
                pre = nums[i]
        if x < 0:
            for i in xrange(0, N//2, 1):
                nums[i], nums[N-1-i] = nums[N-1-i], nums[i]
        else:
            while x < y:
                nums[x], nums[y] = nums[y], nums[x]
                x += 1
                y -= 1
            for j in xrange(i, N, 1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        return nums
