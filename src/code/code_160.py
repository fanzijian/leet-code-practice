#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

要求O(N)且内存占用O(1)

Authors: fanzijian
Date:    2020-06-23 00:18:56
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        p1 = headA
        p2 = headB
        tailA = None
        tailB = None
        while True:
            if p1 == p2:
                return p1
            if not p1.next:
                tailA = p1
            if not p2.next:
                tailB = p2
            if tailA and tailB and tailA != tailB:
                return None
            p1 = p1.next if p1.next else headB
            p2 = p2.next if p2.next else headA
