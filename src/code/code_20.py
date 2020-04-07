#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        char_map = {
            '(': 1,
            ')': -1,
            '{': 2,
            '}': -2,
            '[': 3,
            ']': -3
        }
        length = len(s)
        if length == 0:
            return True
        rst = []
        for i in xrange(0, length, 1):
            if i == 0:
                rst.append(s[i])
            else:
                if len(rst) != 0 and (char_map[rst[-1]] + char_map[s[i]] == 0):
                    rst.pop()
                else:
                    if char_map[s[i]] < 0:
                        return False
                    rst.append(s[i])
        if len(rst) == 0:
            return True
        return False

obj = Solution()
print obj.isValid('{}[]()')


