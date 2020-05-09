#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/

Authors: fanzijian
Date:    2020-05-09 16:50:56

"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            # print stack
            if token in ['+', '-', '*', '/']:
                b = int(stack.pop())
                a = int(stack.pop())
                c = 0
                if token == '+':
                    c = a + b
                if token == '-':
                    c = a - b
                if token == '*':
                    c = a * b
                if token == '/':
                    c = float(a) / b
                stack.append(c)
            else:
                stack.append(token)
        return int(stack.pop())
