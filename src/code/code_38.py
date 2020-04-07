#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""
        sed = "1"
        # if n == 1:
        #     return sed
        while n - 1> 0:
            m = len(sed)
            cnt = 1
            rst = ""
            for i in xrange(0, m, 1):
                if i + 1 < m and sed[i] == sed[i+1]:
                    cnt += 1
                else:
                    rst = '%s%d%s' % (rst, cnt, sed[i])
                    cnt = 1
            sed = rst
            n -= 1
        return sed

obj = Solution()
print obj.countAndSay(1)
