#!/usr/bin/env python
#-*- coding: utf-8 -*-


class Solution(object):
    def totalMethods(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        n_list = [1, 1]
        for i in xrange(1, n, 1):
            tmp = n_list[i] + n_list[i - 1]
            n_list.append(tmp)
        return n_list[-1]

obj = Solution()
print obj.totalMethods(12)