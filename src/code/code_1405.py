#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/longest-happy-string/

思路：贪心算法，优先选择数量最多的，如果数量最多的已经连续两次了，则使用次多的

Authors: fanzijian(fanzijian@baidu.com)
Date:    2020-04-08 19:19:56

"""
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        nums = [(a, 'a'), (b, 'b'), (c, 'c')]
        rst = ""
        cur = 0
        pre = -1
        cnt = 0
        while True:
            nums.sort(key=lambda ele: ele[0], reverse=True)
            # print nums, cnt, cur, pre
            # 全部都处理完毕了，则结束
            if nums[0][0] == 0:
                break
            # 找到最大的
            cur = nums[0][1]
            # 如果已经有连续两个是cur字符了，则选择下一个
            if cur == pre and cnt >= 2:
                # 下一个已经用完了，则结束
                if nums[1][0] == 0:
                    break
                # 下一个没用完，则使用
                cur = nums[1][1]
                # print cur,nums,nums[1],nums[1][0]
                nums[1] = (nums[1][0]-1, nums[1][1])
            else:
                nums[0] = (nums[0][0]-1, nums[0][1])
            # 登记结果
            rst += cur
            # 更新cnt和pre
            if cur == pre:
                cnt += 1
            else:
                cnt = 1
            pre = cur
        return rst


