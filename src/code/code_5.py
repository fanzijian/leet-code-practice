#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/longest-palindromic-substring/

动态规划，马拉车算法？

Authors: fanzijian
Date:    2020-05-19 23:33:56

"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        N = len(s)
        max_sub = [0, 0, 1]
        dp = []
        for i in xrange(0, N, 1):
            dp.append([False for m in xrange(0, N, 1)])
            for j in xrange(i, N, 1):
                if i == j:
                    dp[i][j] = True
                if i == j - 1 and s[i] == s[j]:
                    dp[i][j] = True
                if dp[i][j]:
                    if j - i + 1 > max_sub[2]:
                        max_sub = [i, j, j-i+1]
        # print dp
        for i in xrange(N-1, -1, -1):
            for j in xrange(N-1, -1, -1):
                if i+1 < N and j-1 >= 0 and s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if j - i + 1 > max_sub[2]:
                        max_sub = [i, j, j-i+1]
        return s[max_sub[0]:max_sub[1]+1]
