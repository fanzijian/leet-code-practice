#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_letter_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = []
        for digit in digits:
            tmp_list = digit_letter_map[digit]

            if len(result) == 0:
                result += tmp_list
            else:
                tmp = []
                for d in result:
                    for c in tmp_list:
                        tmp.append(d + c)
                result = tmp
        return list(set(result))

obj = Solution()
print obj.letterCombinations('23')
