#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/

Authors: fanzijian
Date:    2020-05-02 11:23:56

"""
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        rst = []
        for num in candies:
            flag = False
            if num + extraCandies >= max_candies:
                flag = True
            rst.append(flag)
        return rst