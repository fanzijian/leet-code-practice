#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        p = head
        pre = head
        while p:
            if p.val > pre.val:
                pre.next = p
            p = p.next
        return head


