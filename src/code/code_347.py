#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题: https://leetcode-cn.com/problems/top-k-frequent-elements/submissions/

桶排序或者堆排序都行

Authors: fanzijian
Date:    2020-04-16 23:50:56

"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(nums)
        nums_map = {}
        for n in nums:
            if n not in nums_map:
                nums_map[n] = 0
            nums_map[n] += 1

        bulket = [[] for i in range(N+1)]
        for n in nums_map:
            bulket[nums_map[n]].append(n)
        # print bulket
        rst = []
        for i in xrange(0, N+1, 1):
            idx = N - i
            # print idx
            rst.extend(bulket[idx])
            if len(rst) >= k:
                return rst[:k]
        return []
