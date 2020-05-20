#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/zigzag-conversion/

动态规划

Authors: fanzijian
Date:    2020-05-20 23:33:56

"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        rst = ""
        total = len(s)
        T = 2 * numRows - 2
        N = total // T + 1
        # print N, T, total
        for j in xrange(0, numRows, 1):
            for i in xrange(0, N, 1):
                if i*T+j < total:
                    rst += (s[i*T+j])
                if j not in [0, numRows-1] and (i+1)*T-j < total:
                    rst += (s[(i+1)*T-j])
        return rst
