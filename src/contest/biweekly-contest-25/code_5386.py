#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/check-if-a-string-can-break-another-string/

Authors: fanzijian
Date:    2020-05-02 11:23:56

"""
class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = sorted(s1)
        s2 = sorted(s2)
        flag = None
        N = len(s1)
        for i in xrange(0, N, 1):
            if s1[i] == s2[i]:
                continue
            if flag == None:
                flag = s1[i] > s2[i]
            if s1[i] > s2[i] and flag == False:
                return False
            if s1[i] < s2[i] and flag == True:
                return False
        return True


s1 = 'yf'
s2 = 'qm'
obj = Solution()
# print sorted(s1), sorted(s2)
print obj.checkIfCanBreak(s1, s2)
