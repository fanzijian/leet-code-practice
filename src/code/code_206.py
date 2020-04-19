#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题：https://leetcode-cn.com/problems/reverse-linked-list/

Authors: fanzijian
Date:    2020-04-19 16:31:56
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        pre = None
        while p.next:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        p.next = pre
        return p