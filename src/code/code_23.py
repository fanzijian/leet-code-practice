#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题：https://leetcode-cn.com/problems/merge-k-sorted-lists/

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

Authors: fanzijian
Date:    2020-04-19 16:31:56
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        N = len(lists)
        # N个指针，记录各个模块的cur指针
        idx_list = [lists[i] for i in range(N)]
        # 哨兵节点
        slave = ListNode(0)
        new_p = slave
        while True:
            flag = 0
            cnt = 0
            for i in xrange(0, N, 1):
                p = idx_list[i]
                if not p:
                    cnt += 1
                    continue
                if not flag:
                    flag = 1
                    min_p = [i, idx_list[i].val]
                if p.val < min_p[1]:
                    min_p = [i, p.val]
            # 所有都为None
            if not flag:
                break
            new_p.next = idx_list[min_p[0]]
            new_p = new_p.next
            idx_list[min_p[0]] = idx_list[min_p[0]].next
            if cnt == N - 1:
                break
        return slave.next


