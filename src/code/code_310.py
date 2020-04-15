#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题: https://leetcode-cn.com/problems/minimum-height-trees/

类似于广度优先搜索，递归剪枝

Authors: fanzijian(fanzijian@baidu.com)
Date:    2020-04-16 00:07:56

"""
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 处理为1的情况，或者在结束时处理也行
        if n <= 1:
            return [0]
        point_map = {}

        # 整理映射关系，记录拓扑映射
        for e in edges:
            if e[0] not in point_map:
                point_map[e[0]] = []
            if e[1] not in point_map:
                point_map[e[1]] = []
            point_map[e[0]].append(e[1])
            point_map[e[1]].append(e[0])

        # 递归剪枝，将所有的叶子节点剪掉，当剩下1个或者2个节点时，则为最终结果
        while len(point_map.keys()) > 2:
            leaf_point = [e for e in point_map if len(point_map[e]) == 1]
            #  递归剪枝
            for pt in leaf_point:
                for next_pt in point_map[pt]:
                    point_map[next_pt].remove(pt)
                del point_map[pt]
        return point_map.keys()
