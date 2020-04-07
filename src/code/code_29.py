#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 0
        if dividend > 0:
            flag += 1
        else:
            flag -= 1
        if divisor > 0:
            flag += 1
        else:
            flag -= 1
        rst = self.divd(abs(dividend), abs(divisor))
        rst = rst if abs(flag) == 2 else -rst
        if rst > 2147483647:
            rst = 2147483647
        return rst

    def divd(self, dividend, divisor):
        divisor_list = [0]
        n = 0
        j = 0
        while True:
            if dividend < 0:
                j -= 1
                n -= j
                break
            dividend -= divisor_list[j]
            divisor_list.append(divisor_list[j] + divisor)
            n += j
            j += 1
        dividend += divisor_list[j]
        if dividend < divisor:
            return n
        else:
            return n + self.divd(dividend, divisor)

obj = Solution()
print obj.divide(-2147483648, -1)
