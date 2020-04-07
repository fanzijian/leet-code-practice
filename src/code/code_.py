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
        if not head:
            return None
        while head.next:
            if head.val < head.next.val:
                head = head.next
                continue

            cur = slave
            while cur.next.val < head.next.val:
                cur = cur.next
            pre = cur.next
            cur.next = head.next
            tmp = head.next.next
            head.next.next = pre
            head.next = tmp

        return slave.next


h = gen_listNode([0, 5, 3, 4, 1])
obj = Solution()
h = obj.insertionSortList(h)
print_listNode(h)
