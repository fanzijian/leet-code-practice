#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/generate-parentheses/

可以考虑一个一个加符号，当数量达到2*n时，则表示达到给定长度
期间维持l > r , l < n

Authors: fanzijian
Date:    2020-04-06 11:23:56

"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def gen_parentesis(l, r, s):
            if len(s) == 2 * n:
                ans.append(s)
            if l < n:
                s += '('
                gen_parentesis(l+1, r, s)
                s = s[:-1]
            if l > r:
                s += ')'
                gen_parentesis(l, r+1, s)
                s = s[:-1]
        gen_parentesis(0, 0, '')
        return ans
