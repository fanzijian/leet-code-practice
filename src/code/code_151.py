#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/reverse-words-in-a-string/

嗯，内置api真香

Authors: fanzijian(fanzijian@baidu.com)
Date:    2020-04-06 11:23:56

"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        s.reverse()
        s = ' '.join(s)
        return s
