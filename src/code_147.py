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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slave = ListNode(-1)
        slave.next = head
        pre = head
        p = head.next
        while p:
            q = slave
            while q.next != p:
                print q.next.val, p.val, q.val, pre.val
                print_listNode(slave)
                if q.next.val > p.val:
                    tmp = q.next
                    q.next = p
                    pre = p
                    p = p.next
                    print_listNode(slave)
                    print q.next.val, p.val, q.val, tmp.val
                    q.next.next = tmp
                    print_listNode(slave)
                    break
                q = q.next
            if q.next == p:
                pre = p
                p = p.next
        return slave.next


h = gen_listNode([0, 5, 3, 4, 1])
obj = Solution()
h = obj.insertionSortList(h)
print_listNode(h)
