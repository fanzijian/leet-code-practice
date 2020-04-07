# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        slave = ListNode(-1)
        slave.next = head
        low = slave
        up = slave
        i = 0
        while up.next:
            i += 1
            if up.next.val < x:
                if low == up:
                    up = up.next
                    low = low.next
                    continue
                tmp = low.next
                low.next = up.next
                up.next = up.next.next
                low = low.next
                low.next = tmp
                print low.val, tmp.val, up.val, up.next.val
            else:
                up = up.next
            print up.val,i
            print_list_node(slave.next)
        # print_list_node(slave.next)
        head = slave.next
        return head

def gen_list_node(node_list):
    slave = ListNode(-1)
    p = slave
    for i in node_list:
        p.next = ListNode(i)
        p = p.next
    return slave.next

def print_list_node(head):
    rst = []
    while head:
        rst.append(head.val)
        head = head.next
    print rst

node_list = [1, 4, 3, 2, 5]
head = gen_list_node(node_list)
# print_list_node(head)
# s = ListNode(-1)
# s.next = head
obj = Solution()
head = obj.partition(head, 3)
print_list_node(head)

