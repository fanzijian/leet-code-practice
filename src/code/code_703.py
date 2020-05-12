#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/

Authors: fanzijian
Date:    2020-5-12 13:46:56

"""
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = [0]
        N = len(nums)
        self.k = k
        for num in nums:
            self.add(num)

    def heapify_down(self, i, N):
        min_idx = i
        while i <= N:
            if i*2 <= N and self.heap[i*2] < self.heap[min_idx]:
                min_idx = i * 2
            if i*2+1 <= N and self.heap[i*2+1] < self.heap[min_idx]:
                min_idx = i * 2 + 1
            if i == min_idx:
                break
            else:
                self.heap[i], self.heap[min_idx] = self.heap[min_idx], self.heap[i]
                i = min_idx

    def heapify_up(self, i, N):
        fa_idx = i // 2
        while fa_idx > 0 and self.heap[fa_idx] > self.heap[i]:
            self.heap[i], self.heap[fa_idx] = self.heap[fa_idx], self.heap[i]
            i = fa_idx
            fa_idx = i // 2

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        N = min(len(self.heap) - 1, self.k)
        if N < self.k:
            self.heap.append(val)
            self.heapify_up(N+1, N+1)
        else:
            if self.heap[1] < val:
                self.heap[1] = val
                self.heapify_down(1, self.k)
        return self.heap[1]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)