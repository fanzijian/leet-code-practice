#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/target-sum/

Authors: fanzijian
Date:    2020-05-08 16:50:56

"""
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # key表示总和，value表示方法数
        pre = {0: 1}
        cur = {}
        for num in nums:
            # 遍历所有当前的和
            for pre_sum in pre.keys():
                # 因为下一层可能有两种方法
                for cur_sum in [pre_sum + num, pre_sum - num]:
                    # 不存在则新建
                    if cur_sum not in cur:
                        cur[cur_sum] = 0
                    # 累计能够达到cur_sum的方案总数量
                    cur[cur_sum] += pre[pre_sum]
            pre = cur
            cur = {}
        return pre[S] if S in pre else 0
