#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda val: val[0])
        rst = [intervals[0]]
        for cell in intervals:
            pre = rst[-1]
            if cell[0] > pre[1]:
                rst.append(cell)
            else:
                pre[1] = max(pre[1], cell[1])
        return rst
