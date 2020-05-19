#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/video-stitching/

贪心算法&动态规划

Authors: fanzijian
Date:    2020-05-19 23:33:56

"""
class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        step_map = {}
        for clip in clips:
            if clip[0] not in step_map:
                step_map[clip[0]] = 0
            step_map[clip[0]] = max(step_map[clip[0]], clip[1])
        start = 0
        end = 0
        cnt = 0
        # print step_map
        while end < T:
            max_end = end
            cnt += 1
            for i in xrange(start, end+1, 1):
                if i in step_map and max_end < step_map[i]:
                    max_end = step_map[i]
            # print start, end, max_end
            start = end
            if end == max_end:
                return -1
            end = max_end
        return cnt
