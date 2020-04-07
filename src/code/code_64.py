#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        pre_list = []
        for i in xrange(0, n, 1):
            tmp = grid[0][i] + (pre_list[-1] if len(pre_list) != 0 else 0)
            pre_list.append(tmp)
        cur_list = pre_list
        print pre_list
        for i in xrange(1, m, 1):
            cur_list = [min(pre_list[j], cur_list[j-1] if j > 0 else pre_list[j]) + grid[i][j] for j in xrange(0, n, 1)]
            pre_list = cur_list
            print pre_list
        return cur_list[-1]


obj = Solution()
print obj.minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
])
