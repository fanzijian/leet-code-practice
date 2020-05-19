#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/

动态规划

Authors: fanzijian
Date:    2020-05-19 23:33:56

"""
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        M = len(matrix)
        N = len(matrix[0])
        total = 0
        for i in xrange(0, M, 1):
            for j in xrange(0, N, 1):
                if i - 1 >= 0 and j - 1 >= 0:
                    if matrix[i][j] > 0:
                        matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1],matrix[i-1][j]) + 1
                total += matrix[i][j]
        return total