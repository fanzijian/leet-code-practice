#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/max-difference-you-can-get-from-changing-an-integer/submissions/

Authors: fanzijian
Date:    2020-05-03 11:23:56

"""
class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        ss = str(num)
        max_num = ['', '', '']
        min_num = ['', '', '']
        for i in xrange(0, len(ss), 1):
            if i == 0 and ss[i] != '1':
                min_num[0] = ss[i]
                min_num[1] = '1'
            if i != 0 and ss[i] not in ['0', '1'] and not min_num[0]:
                min_num[0] = ss[i]
                min_num[1] = '0'

            min_num[2] += min_num[1]  if ss[i] == min_num[0] else ss[i]

            if ss[i] != '9' and not max_num[0]:
                max_num[0] = ss[i]
                max_num[1] = '9'
            max_num[2] += max_num[1] if ss[i] == max_num[0] else ss[i]
        print min_num, max_num
        return int(max_num[2]) - int(min_num[2])

obj = Solution()
print obj.maxDiff(9288)
