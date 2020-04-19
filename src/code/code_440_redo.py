#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题：https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/


Authors: fanzijian
Date:    2020-04-19 22:31:56
"""


class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def get_count(n, prefix):
            cur = prefix
            cur2 = prefix + 1
            count = 0
            while cur <= n:
                count += min(cur2, n+1) - cur
                cur *= 10
                cur2 *= 10
            return count
        p = 1
        prefix = 1
        while p < k:
            count = get_count(n, prefix)
            if p + count <= k:
                p += count
                prefix += 1
            else:
                p += 1
                prefix *= 10
        return prefix
