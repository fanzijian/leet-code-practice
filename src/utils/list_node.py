class ListNode(object):
    """[单向链表节点]
    """
    def __init__(self, x):
        """[初始化]
        """
        self.val = x
        self.next = None


def gen_list_node(nums):
    """[接受数组，返回一个初始化完毕的链表头节点]
    """
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


def print_list_node(head):
    """[遍历并打印链表所有元素，并返回元素value的列表]
    """
    rst = []
    while head:
        rst.append(head.val)
        head = head.next
    print rst
    return rst
