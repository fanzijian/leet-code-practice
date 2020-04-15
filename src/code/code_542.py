#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题: https://leetcode-cn.com/problems/01-matrix/

原址修改，首先遍历，找到所有的1，然后处理所有的1，如果1的上下左右都是>=1的，则将该值修改为2
处理完之后，再处理所有的2，以此类推

Authors: fanzijian(fanzijian@baidu.com)
Date:    2020-04-15 23:00:56

"""
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        is_visited = set()
        N = len(matrix)
        M = len(matrix[0])
        def check_uniq(i, j, cnt, queue):
            if matrix[i][j] < cnt:
                return
            if i-1 >= 0 and matrix[i-1][j] < cnt:
                return
            if i+1 < N and matrix[i+1][j] < cnt:
                return
            if j-1 >= 0 and matrix[i][j-1] < cnt:
                return
            if j+1 < M and matrix[i][j+1] < cnt:
                return
            matrix[i][j] += 1
            queue.add((i, j))

        queue = set([(i, j) for i in xrange(0, N, 1) for j in xrange(0, M, 1) if matrix[i][j] == 1])

        index = 0

        while queue:
            process_set = queue.copy()
            queue = set()
            index += 1
            while process_set:
                i,j = process_set.pop()
                check_uniq(i, j, index, queue)
        return matrix



