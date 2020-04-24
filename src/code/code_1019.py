#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/next-greater-node-in-linked-list/

维护一个list，当中存储index和原链表的指针
遍历链表，对比当前的cur.val和list中的情况，
将list中所有val小于cur.val的，对应index的结果更新为cur.val即可

Authors: fanzijian
Date:    2020-04-12 11:23:56

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not head:
            return []
        index = 0
        rst = []
        cur = head
        pre = None
        while cur:
            rst.append(0)
            while pre:
                if pre.val[1].val < cur.val:
                    rst[pre.val[0]] = cur.val
                    pre = pre.next
                else:
                    new_node = ListNode([index, cur])
                    new_node.next = pre
                    pre = new_node
                    break
            if not pre:
                pre = ListNode([index, cur])
            cur = cur.next
            index += 1
        return rst