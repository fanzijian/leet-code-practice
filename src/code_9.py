#!/usr/bin/env python
#-*- coding: utf-8 -*-
import math

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        count = ""
        length = len(s)

        palindrome = set()

        # 所有的1阶点都是回文字符串，
        # 所有字符相同的2阶点都是回文字符串
        # 所有高阶点如果是回文字符串，那么他的去掉他的首位，那也是回文字符串
        # 筛选记录所有种子点的中心位置
        last_result = s[0]
        for i in range(length):
            palindrome.add(i)
            if i == 0:
                continue
            if s[i-1] == s[i]:
                palindrome.add(i-0.5)
                last_result = s[i-1:i+1]

        # 开始层级遍历，筛选更高阶的回文字符串
        level = 1
        while True:
            tmp = set()
            for seed in palindrome:
                result = self.checkPalindrome(s, seed, level)
                if result:
                    print seed, level, result
                    last_result = result if len(result) > len(last_result) else last_result
                    tmp.add(seed)
            if len(tmp) == 0:
                break
            #     for seed in palindrome:
            #         print s, seed, level
            #         print self.checkPalindrome(s, seed, level-1)
            #     return None
            level += 1
            palindrome = tmp
        return last_result

    def checkPalindrome(self, s, mid, level):
        length = len(s)
        if mid % 1 == 0:
            # 种子为1阶
            start = int(mid - level)
            end = int(mid + level)
        else:
            # 种子为2阶
            start = int(math.floor(mid) - level)
            end = int(math.ceil(mid) + level)
        if start >= 0 and end < length and s[start] == s[end]:
            return s[start: end+1]
        return False


obj = Solution()

print obj.longestPalindrome("aaba")
# babad
