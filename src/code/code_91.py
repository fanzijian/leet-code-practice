#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if s[0] == '0':
            return 0
        dp = [1, 1]
        rst = 1
        for i in xrange(1, length, 1):
            val = int(s[i-1:i+1])
            tmp = dp[i]
            if val <= 26 and int(s[i]) != 0 and int(s[i-1]) != 0:
                if (i+1) >= length or ((i+1) < length and int(s[i+1]) != 0):
                    tmp = dp[i] + dp[i-1]
            if int(s[i]) == 0 and val not in [10, 20]:
                rst = 0
                print 'break'
                break
            dp.append(tmp)
        if rst != 0:
            rst = dp[-1]
        print dp
        return rst

obj = Solution()
print obj.numDecodings("110")
