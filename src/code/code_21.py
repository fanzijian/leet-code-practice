#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)
        head = p
        while (l1 != None and l2 != None):
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l2 if l1 == None else l1
        return head.next


def print_list_node(p):
    rst = []
    while p.next:
        rst.append(p.val)
        p = p.next
    rst.append(p.val)
    print rst

def gen_list_node_from_list(p):
    head = ListNode(0)
    k = head
    for i in range(len(p)):
        k.val = p[i]
        if i < len(p) - 1:
            k.next = ListNode(0)
            k = k.next
    k.next = None
    return head

l1 = gen_list_node_from_list([1])
l2 = gen_list_node_from_list([2])
obj = Solution()
p = obj.mergeTwoLists(l1, l2)

print_list_node(p)


