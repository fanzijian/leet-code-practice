#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/destination-city/

Authors: fanzijian
Date:    2020-05-03 11:23:56

"""
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        if not paths:
            return None
        position = paths[0][0]
        route_map = {}
        for path in paths:
            if path[0] not in route_map:
                route_map[path[0]] = ''
            route_map[path[0]] = path[1]
            while position in route_map:
                position = route_map[position]
        return position