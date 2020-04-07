class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode((l1.val + l2.val) % 10)
        default = ListNode(0)
        p = head
        up = (l1.val + l2.val) / 10
        while 1:
            if not (l1.next or l2.next or up):
                break
            l1 = l1.next if l1.next != None else default
            l2 = l2.next if l2.next != None else default
            val = l1.val + l2.val + up
            up = val / 10

            p.next = ListNode(val % 10)
            print val, up, val % 10
        return head


l1 = [5]
l2 = [5]
def list2listNode(l1):
    head = ListNode(l1[0])
    if len(l1) == 1:
        return head
    p = head
    for i in range(1,len(l1), 1):
        p.next = ListNode(l1[i])
        p = p.next
    return head


l1 = list2listNode(l1)
l2 = list2listNode(l2)
obj = Solution()
result =  obj.addTwoNumbers(l1, l2)
