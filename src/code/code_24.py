#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

1. 你的算法只能使用常数的额外空间
2. 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

todo 可以用每次的前置节点来作为k个元素遍历的哨兵节点

Authors: fanzijian(fanzijian)
Date:    2020-04-22 15:50:56

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(p, end):
            #反转链表
            slave = ListNode(-1)
            slave.next = p
            pre = slave
            while p != end:
                tmp = p.next
                p.next = pre
                pre = p
                p = tmp
            p.next = pre
            tail = slave.next
            slave.next = p
            return slave.next, tail

        slave = ListNode(-1)
        slave.next = head
        pre = slave
        p0 = p1 = head
        i = 1
        while True:
            # 找到第k个节点
            while p1 and p1.next and i < k:
                p1 = p1.next
                i += 1
            if i != k or not p1:
                # 最后不足k个，或者p1为空，结束
                break
            next_p = p1.next
            new_head, new_tail = reverse(p0, p1)
            pre.next = new_head
            new_tail.next = next_p
            pre = new_tail
            i = 1
            p0 = p1 = next_p

        return slave.next
