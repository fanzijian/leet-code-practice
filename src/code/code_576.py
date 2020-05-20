#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/out-of-boundary-paths/

动态规划

Authors: fanzijian
Date:    2020-05-20 23:33:56

"""
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        cnt = 0
        dp = [[0 for y in xrange(0, n, 1)] for x in xrange(0, m, 1)]
        dp[i][j] = 1
        queue = [(i, j)]
        count = 0
        for i in xrange(0, N, 1):
            next_queue = set()
            temp = [[0 for y in xrange(0, n, 1)] for x in xrange(0, m, 1)]
            while queue:
                x,y = queue.pop()
                if x > 0:
                    temp[x-1][y] += dp[x][y]
                    next_queue.add((x-1, y))
                else:
                    count += dp[x][y]
                if y > 0:
                    temp[x][y-1] += dp[x][y]
                    next_queue.add((x, y-1))
                else:
                    count += dp[x][y]
                if x < m-1:
                    temp[x+1][y] += dp[x][y]
                    next_queue.add((x+1, y))
                else:
                    count += dp[x][y]
                if y < n-1:
                    temp[x][y+1] += dp[x][y]
                    next_queue.add((x, y+1))
                else:
                    count += dp[x][y]
            count %= (10**9 + 7)
            queue = next_queue
            dp = temp
        return count



