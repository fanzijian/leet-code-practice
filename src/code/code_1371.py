#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/submissions/

动态规划&位运算&状态机

Authors: fanzijian
Date:    2020-05-20 23:33:56

"""
class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [-1 for i in xrange(0, 32, 1)]
        dp[0] = 0
        total = 0
        max_len = 0
        for i in xrange(0, len(s), 1):
            status = 0
            if s[i] == 'a':
                status += 1
            if s[i] == 'e':
                status += 1 << 1
            if s[i] == 'i':
                status += 1 << 2
            if s[i] == 'o':
                status += 1 << 3
            if s[i] == 'u':
                status += 1 << 4
            total ^= status
            if dp[total] == -1:
                dp[total] = i + 1
            else:
                max_len = max(max_len, i - dp[total] + 1)
        return max_len


