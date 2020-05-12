#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目：https://leetcode-cn.com/problems/min-stack/

Authors: fanzijian
Date:    2020-5-12 13:46:56

"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.data = []
        self.min_data = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.count += 1
        self.data.append(x)
        min_val = x
        if self.min_data and min_val > self.min_data[-1]:
            min_val = self.min_data[-1]
        self.min_data.append(min_val)

    def pop(self):
        """
        :rtype: None
        """
        if self.count == 0:
            return None
        self.count -= 1
        self.min_data.pop()
        return self.data.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.count == 0:
            return None
        return self.data[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if self.count == 0:
            return None
        return self.min_data[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()