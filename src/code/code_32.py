#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/longest-valid-parentheses/
例如：")()())()()("
Authors: fanzijian
Date:    2020-05-09 18:40:56

"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        stack = []
        for i in xrange(0, len(s), 1):
            if s[i] == '(':
                stack.append('(')
            else:
                cur_len = 0
                flag = 0
                while stack:
                    val = stack.pop()
                    if val == '(':
                        if flag:
                            stack.append('(')
                            break
                        else:
                            flag = 1
                            cur_len += 2
                    else:
                        cur_len += val
                stack.append(cur_len)
                if not flag:
                    stack = []
                max_len = max(max_len, cur_len)
            # print stack
        return max_len
