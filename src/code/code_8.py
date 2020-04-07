#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = -1
        start = False
        rst = ""
        while True:
            i += 1
            if i >= len(str):
                break
            if str[i] == ' ':
                if not start:
                    continue
                else:
                    break
            if str[i] in ['+', '-', '0','1','2','3','4','5','6','7','8','9']:
                if not start:
                    start = True
                elif str[i] in ['+', '-']:
                    break
                rst += str[i]
            else:
                break
        rst = 0 if ((len(rst) == 1 and rst[0] in ['+', '-']) or len(rst) == 0) else int(rst)
        if rst > 2 ** 31:
            rst = 2 ** 31
            # return 'INT_MAX (231 − 1)'
        if rst < -2 ** 31:
            rst = -2 ** 31
            # return 'INT_MIN (231 − 1)'
        return rst

obj = Solution()
print obj.myAtoi("-91283472332")
