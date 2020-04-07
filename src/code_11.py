#!/usr/bin/env python
#-*- coding: utf-8 -*-


class Solution(object):
    """[]
    从两端分别遍历：
    1. 记录当前最大面积max_area，起始位置b，结束位置e
    2. tmp_area = min(height[b],height[e]) * (e - b)
    3. if tmp_area > max_area, 则max_area = tmp_area; else 则较矮的一边序号变动1（左边则+1，右边则-1）
    """

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        b = 0
        e = len(height) - 1
        while True:
            tmp_area = min(height[b], height[e]) * (e - b)
            if tmp_area > max_area:
                max_area = tmp_area
            else:
                if height[b] > height[e]:
                    e -= 1
                else:
                    b += 1
            if e <= b:
                break
        return max_area

obj = Solution()
print obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
