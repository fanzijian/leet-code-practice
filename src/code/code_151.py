#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/reverse-words-in-a-string/

模拟原地处理

Authors: fanzijian
Date:    2020-05-12 11:23:56

"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(ss, i, j):
            while i < j:
                ss[i], ss[j] = ss[j], ss[i]
                i += 1
                j -= 1
        s = s.strip()
        if not s:
            return ""
        pre = s[0]
        ss = []
        for i in xrange(0, len(s), 1):
            if s[i] == ' ' and pre == ' ':
                continue
            ss.append(s[i])
            pre = s[i]
        i = 0
        j = len(ss) - 1
        reverse(ss, i, j)
        i = 0
        j = 0
        while j < len(ss):
            while j < len(ss) and ss[j] != ' ':
                j += 1
            reverse(ss, i, j-1)
            j += 1
            i = j
        return ''.join(ss)

