#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        f(m,n) = f(m, n-1) + f(m-1, n)
        """
        rst = [[1 for i in range(n)]]
        for i in xrange(1, m, 1):
            rst.append([0 for x in range(n)])
            for j in xrange(0, n, 1):
                if j == 0:
                    rst[i][j] = 1
                else:
                    rst[i][j] = rst[i][j-1] + rst[i-1][j]
        return rst[m-1][n-1]

obj = Solution()
print obj.uniquePaths(3,2)