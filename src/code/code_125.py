#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check_is_digit_word(w):
            w = ord(w)
            return (w >= ord('0') and w <= ord('9')) or (w >= ord('a') and w <= ord('z'))

        s = s.lower()
        p = [0, len(s) - 1]
        length = len(s)
        while p[0] < p[1]:
            while p[0] < length and not check_is_digit_word(s[p[0]]):
                p[0] += 1
            while p[1] > 0 and not check_is_digit_word(s[p[1]]):
                p[1] -= 1
            if p[0] >= p[1]:
                break
            if s[p[0]] != s[p[1]]:
                return False
            p[0] += 1
            p[1] -= 1
        return True


obj = Solution()
print obj.isPalindrome(",.")
