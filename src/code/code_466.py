#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题：https://leetcode-cn.com/problems/count-the-repetitions/

Authors: fanzijian
Date:    2020-04-19 14:28:56

"""
class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if n1 == 0:
            return 0
        # 首先判断s2中是否存在s1中不存在的字符，如果有，则直接返回0
        # 贪心算法，遍历n个s1才能与m个s2完全匹配（循环节），则计算n1和n的倍数，则 M = n1 // n * m
        # 然而循环节并不总是从0开始的...
        # 因此需要使用map登记和s1的最后字符匹配位置对应的s2的index，当出现重复时，则表示出现了循环节
        # 同时，针对最后尾部不足循环节的部分，需要遍历处理,处理是index别弄错了，要沿着之前的开始
        idx, lv_s1, lv_s2 = [0, 0, 0]
        idx_map = {}
        while True:
            lv_s1 += 1
            for s in s1:
                if s == s2[idx]:
                    idx += 1
                    if idx == len(s2):
                        lv_s2 += 1
                        idx = 0
            if lv_s1 == n1:
                return lv_s2 // n2

            if idx in idx_map:
                pre_loop = idx_map[idx]
                # 每lv_s1 - pre_loop[0]个s1对应lv_s2 - pre_loop[1]个s2
                loop = (lv_s1 - pre_loop[0], lv_s2 - pre_loop[1])
                break
            else:
                idx_map[idx] = (lv_s1, lv_s2)
        print idx, lv_s1, lv_s2, idx_map
        M = pre_loop[1] + (n1 - pre_loop[0]) // loop[0] * loop[1]
        reset = (n1 - pre_loop[0]) % loop[0]

        for i in range(reset):
            for s in s1:
                if s2[idx] == s:
                    idx += 1
                    if idx >= len(s2):
                        M += 1
                        idx = 0
        return M / n2


obj = Solution()

print obj.getMaxRepetitions('baba', 11, 'baab', 1)



