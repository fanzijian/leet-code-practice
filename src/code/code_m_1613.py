#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/intersection-lcci/

额，处理情况比想象中要麻烦的多得多。。。
Authors: fanzijian
Date:    2020-04-12 11:23:56

"""


class Solution(object):
    def intersection(self, start1, end1, start2, end2):
        """
        :type start1: List[int]
        :type end1: List[int]
        :type start2: List[int]
        :type end2: List[int]
        :rtype: List[float]
        """
        def inside(x1, y1, x2, y2, xk, yk):
            # 若与 x 轴平行，只需要判断 x 的部分
            # 若与 y 轴平行，只需要判断 y 的部分
            # 若为普通线段，则都要判断
            return (x1 == x2 or min(x1, x2) <= xk <= max(x1, x2)) and (y1 == y2 or min(y1, y2) <= yk <= max(y1, y2))

        def update(ans, xk, yk):
            # 将一个交点与当前 ans 中的结果进行比较
            # 若更优则替换
            return [xk, yk] if not ans or [xk, yk] < ans else ans

        x1, y1 = start1
        x2, y2 = end1
        x3, y3 = start2
        x4, y4 = end2

        ans = list()
        # 判断 (x1, y1)~(x2, y2) 和 (x3, y3)~(x4, y3) 是否平行
        if (y4 - y3) * (x2 - x1) == (y2 - y1) * (x4 - x3):
            # 若平行，则判断 (x3, y3) 是否在「直线」(x1, y1)~(x2, y2) 上
            if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                # 判断 (x3, y3) 是否在「线段」(x1, y1)~(x2, y2) 上
                if inside(x1, y1, x2, y2, x3, y3):
                    ans = update(ans, x3, y3)
                # 判断 (x4, y4) 是否在「线段」(x1, y1)~(x2, y2) 上
                if inside(x1, y1, x2, y2, x4, y4):
                    ans = update(ans, x4, y4)
                # 判断 (x1, y1) 是否在「线段」(x3, y3)~(x4, y4) 上
                if inside(x3, y3, x4, y4, x1, y1):
                    ans = update(ans, x1, y1)
                # 判断 (x2, y2) 是否在「线段」(x3, y3)~(x4, y4) 上
                if inside(x3, y3, x4, y4, x2, y2):
                    ans = update(ans, x2, y2)
            # 在平行时，其余的所有情况都不会有交点
        else:
            # 联立方程得到 t1 和 t2 的值
            t1 = float(x3 * (y4 - y3) + y1 * (x4 - x3) - y3 * (x4 - x3) -
                       x1 * (y4 - y3)) / ((x2 - x1) * (y4 - y3) - (x4 - x3) * (y2 - y1))
            t2 = float(x1 * (y2 - y1) + y3 * (x2 - x1) - y1 * (x2 - x1) -
                       x3 * (y2 - y1)) / ((x4 - x3) * (y2 - y1) - (x2 - x1) * (y4 - y3))
            # 判断 t1 和 t2 是否均在 [0, 1] 之间
            if 0.0 <= t1 <= 1.0 and 0.0 <= t2 <= 1.0:
                ans = [x1 + t1 * (x2 - x1), y1 + t1 * (y2 - y1)]

        return ans
