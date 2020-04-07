#!/usr/bin/env python
#-*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def gen_listNode(nums):
    head = None
    p = None
    for val in nums:
        if not p:
            head = ListNode(val)
            p = head
        else:
            p.next = ListNode(val)
            p = p.next
    return head


def print_listNode(head):
    rst = []
    while head:
        rst.append(head.val)
        head = head.next
    print rst
    return rst

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def get_list_node_mid(head):
            p0, p1 = head, head
            pre = None
            while p0 and p0.next:
                if not pre:
                    pre = head
                else:
                    pre = pre.next
                p0 = p0.next.next
                p1 = p1.next
            return p1, pre

        def merge(p1, p2):
            head = p1 if p1.val < p2.val else p2
            p = None
            while p1 and p2:
                tmp = p1 if p1.val < p2.val else p2
                if not p:
                    p = tmp
                else:
                    p.next = tmp
                    p = p.next
                if p1.val < p2.val:
                    p1 = p1.next
                else:
                    p2 = p2.next
            if p1:
                p.next = p1
            if p2:
                p.next = p2
            return head


        if not head.next:
            return head
        # 切分成两个链表
        mid, pre = get_list_node_mid(head)
        pre.next = None
        head = self.sortList(head)
        mid = self.sortList(mid)
        rst = merge(mid, head)
        return rst


obj = Solution()
h = gen_listNode([4, 2, 1, 3])
# print_listNode(h)
print_listNode(obj.sortList(gen_listNode(
    [4, 2, 1, 3])))


def merge(p1, p2):
    head = p1 if p1.val < p2.val else p2
    p = None
    while p1 and p2:
        tmp = p1 if p1.val < p2.val else p2
        if not p:
            p = tmp
        else:
            p.next = tmp
            p = p.next
        if p1.val < p2.val:
            p1 = p1.next
        else:
            p2 = p2.next

    if p1:
        p.next = p1
    if p2:
        p.next = p2
    return head


h = gen_listNode([1, 3])
h2 = gen_listNode([2,4])
rst = merge(h, h2)
print_listNode(rst)
