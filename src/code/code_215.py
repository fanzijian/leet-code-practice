#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/submissions/

Authors: fanzijian
Date:    2020-5-12 13:46:56

"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = nums[:k]
        heapq.heapify(heap)
        for i in xrange(k, len(nums), 1):
            heapq.heappushpop(heap, nums[i])
        return heap[0]