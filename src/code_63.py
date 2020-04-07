#!/usr/bin/env python
#-*- coding: utf-8 -*-


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int

        障碍物可以当作0来处理，那么，方法则与原方案差不多复杂度 O(m*n)
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        pre_list = []
        for val in obstacleGrid[0]:
            tmp = 0
            if val == 0 and len(pre_list) != 0 and pre_list[-1] != 0:
                tmp = 1
            if len(pre_list) == 0 and val == 0:
                tmp = 1
            pre_list.append(tmp)
        cur_list = pre_list
        for i in xrange(1, m, 1):
            cur_list = [1 if j == 0 else 0 for j in obstacleGrid[i]]
            if pre_list[0] == 0:
                cur_list[0] = 0
            for j in xrange(1, n, 1):
                cur_list[j] = (cur_list[j-1] + pre_list[j]) if cur_list[j] != 0 else 0
            pre_list = cur_list
        return cur_list[-1]

obj = Solution()
print obj.uniquePathsWithObstacles(
    [[0, 0, 0], [0, 1, 0], [0, 0, 0]])

