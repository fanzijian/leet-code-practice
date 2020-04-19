#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
最大堆

Authors: fanzijian
Date:    2020-04-19 13:46:56

"""
class Heap(object):
    # 最大堆
    def __init__(self, size):
        self.heap = [-1]
        self.size = size
        self.count = 0

    def pop(self):
        """[pop]
        """
        if self.count == 0:
            return None
        self.heap[0] = self.heap[1]
        self.count -= 1
        self.heap[1] = self.heap[self.count+1]
        self._heapify()
        return self.heap[0]

    def push(self, val):
        """[push]
        """
        if self.count >= self.size:
            return False
        self.count += 1
        self.heap.append(val)
        i = self.count
        while i//2 > 0 and self.heap[i] > self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i // 2
        return True

    def _heapify(self):
        """[自上而下的堆化]
        """
        i = 1
        while True:
            max_pos = i
            if (i*2 <= self.count and self.heap[i] < self.heap[i*2]):
                max_pos = i * 2
            if (i*2+1 <= self.count and self.heap[i] < self.heap[i*2+1]):
                max_pos = i * 2 + 1
            if i == max_pos:
                break
            self.heap[i], self.heap[max_pos] = self.heap[max_pos], self.heap[i]
            i = max_pos

    def visual(self):
        """[按层可视化]
        """
        level = 1
        level_data = []
        for i in xrange(1, self.count+1, 1):
            if i  > 2 ** level - 1:
                level += 1
                print level_data
                level_data = []
            level_data.append(self.heap[i])
        print level_data

obj = Heap(10)
a = [obj.push(10-i) for i in range(10)]
obj.visual()

