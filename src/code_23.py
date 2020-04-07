# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        p = head
        head = p.next
        while p.next:
            p1 = p.next
            tmp = p1.next
            p1.next = p
            p.next = tmp


