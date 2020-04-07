#!/usr/bin/env python
#-*- coding: utf-8 -*-
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head
        i = 0
        k = head
        while p.next:
            if i>=n:
                k = k.next
            p = p.next
            i+=1
        if i < n:
            head = head.next
        else:
            k.next = k.next.next if k.next.next else None
        return head

def print_list_node(p):
    rst = []
    while p.next:
        rst.append(p.val)
        p = p.next
    rst.append(p.val)
    print rst

obj = Solution()
head = ListNode(1)
p = head
for i in range(5):
    p.next = ListNode(i+2)
    p = p.next

print_list_node(head)

k = obj.removeNthFromEnd(head, 1)

print_list_node(k)

