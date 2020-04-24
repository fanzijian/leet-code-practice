#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/generate-parentheses/

共有 l=n 个 '(' 以及 r=n 个 ')'，递归选择左括号或者右括号，当l==r==0时，添加到结果集合中，
当保证每次选择，l>=r同时l>=0 且 r>=0

Authors: fanzijian
Date:    2020-04-06 11:23:56

"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []

        def genParenth(l, r, strs):
            if l == 0 and r == 0:
                return strs
            if l == 0 and r != 0:
                rst = []
                for s in strs:
                    s += ")" * r
                    rst.append(s)
                return rst
            if l == r:
                rst = []
                for s in strs:
                    s += "("
                    rst.append(s)
                return genParenth(l-1, r, rst)
            if l < r:
                rst1 = []
                rst2 = []
                for s in strs:
                    rst1.append(s+"(")
                    rst2.append(s+")")
                return genParenth(l-1, r, rst1) + genParenth(l, r-1, rst2)

        return genParenth(n, n, [""])
