#!/usr/bin/env python
#-*- coding: utf-8 -*-


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_int_map = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        s = ''
        lv = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for i in range(len(lv)):
            while True:
                if num < lv[i]:
                    break
                s += roman_int_map[lv[i]]
                num -= lv[i]
        return s

obj = Solution()
print obj.intToRoman(9)
