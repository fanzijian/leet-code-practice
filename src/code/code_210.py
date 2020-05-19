#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/course-schedule-ii/

深度优先（广度优先遍历）结合

Authors: fanzijian
Date:    2020-05-17 23:33:56

"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        course_map = {}
        req_map = {}
        for pre_course in prerequisites:
            if pre_course[0] not in course_map:
                course_map[pre_course[0]] = 0
            course_map[pre_course[0]] += 1
            if pre_course[1] not in req_map:
                req_map[pre_course[1]] = []
            req_map[pre_course[1]].append(pre_course[0])
        queue = [i for i in xrange(0, numCourses, 1) if i not in course_map]
        rst = []
        while queue:
            course = queue.pop()
            rst.append(course)
            if course in req_map:
                for row in req_map[course]:
                    course_map[row] -= 1
                    if course_map[row] == 0:
                        queue.append(row)
        return rst if len(rst) == numCourses else []


