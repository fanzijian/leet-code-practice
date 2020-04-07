#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Solution(object):
    def romanToInt(self, s):
        """
        从左向右遍历，当遍历到底位在高位前时，则需要-1
        :type s: str
        :rtype: int
        """
        roman_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0
        length = len(s)
        for i in range(length):
            n = roman_int_map[s[i]]
            if i < length - 1:
                if n < roman_int_map[s[i + 1]]:
                    n = -n
            num += n
            # print num, n
        return num


obj = Solution()
print obj.romanToInt("IXLVIII")
