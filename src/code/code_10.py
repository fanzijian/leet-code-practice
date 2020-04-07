#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str regex
        :rtype: bool
        todo: 虽然AC了，但是用递归写的，没有使用动态规划，部分地方逻辑需要进一步梳理
        """
        if len(s) + len(p) == 0:
            return True
        if len(p) == 0:
            return False
        while True:
            if p[-1] == '*':
                if len(s) > 0 and (p[-2] == s[-1] or p[-2] == '.'):
                    return self.isMatch(s[:-1], p) or self.isMatch(s, p[:-1]) or self.isMatch(s, p[: -2])
                else:
                    return self.isMatch(s, p[:-2])
            if len(s) > 0 and (p[-1] == s[-1] or p[-1] == '.'):
                return self.isMatch(s[:-1], p[:-1])
            return False

obj = Solution()
print obj.isMatch('', 'a*')


