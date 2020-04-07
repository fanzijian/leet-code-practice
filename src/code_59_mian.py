class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class MaxQueue(object):

    def __init__(self):
        self.max_node = None
        self.size = 0
        self.head = None
        self.tail = None

    def max_value(self):
        """
        :rtype: int
        """
        return self.max_node.val if self.size != 0 else -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.max_node = new_node
        else:
            if self.max_node.val <= value:
                self.max_node = new_node
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop_front(self):
        """
        :rtype: int
        """
        if self.size == 0:
            return -1
        val = self.head.val
        if self.size == 1:
            self.head = None
            self.tail  = None
            self.max_node = None
        else:
            if self.max_node == self.head:
                p = self.head.next
                self.max_node = p
                while p:
                    if self.max_node.val <= p.val:
                        self.max_node = p
                    p = p.next
            self.head = self.head.next
        self.size -= 1
        return val


obj = MaxQueue()

func_map = {
    'max_value': obj.max_value,
    'pop_front': obj.pop_front,
    'push_back': obj.push_back
}

func_list = ["MaxQueue", "max_value", "pop_front", "pop_front", "max_value", "max_value", "pop_front", "pop_front", "push_back", "pop_front", "pop_front", "max_value", "push_back", "max_value", "push_back", "push_back", "max_value", "pop_front", "pop_front", "push_back", "push_back", "push_back", "push_back", "push_back", "pop_front", "pop_front", "push_back", "pop_front", "max_value", "max_value", "max_value", "max_value", "pop_front", "max_value", "pop_front", "push_back", "push_back", "pop_front", "pop_front", "pop_front", "push_back", "max_value", "pop_front", "push_back", "pop_front", "pop_front", "push_back", "max_value", "push_back", "push_back",
             "pop_front", "pop_front", "max_value", "pop_front", "push_back", "push_back", "pop_front", "push_back", "pop_front", "max_value", "push_back", "max_value", "max_value", "pop_front", "push_back", "pop_front", "push_back", "push_back", "max_value", "max_value", "max_value", "pop_front", "max_value", "pop_front", "push_back", "push_back", "pop_front", "max_value", "push_back", "pop_front", "pop_front", "pop_front", "push_back", "push_back", "push_back", "max_value", "pop_front", "push_back", "push_back", "max_value", "max_value", "pop_front", "pop_front", "max_value", "pop_front", "max_value", "pop_front", "max_value", "push_back", "max_value"]
arg_list = [[], [], [], [], [], [], [], [], [450], [], [], [], [717], [], [567], [383], [], [], [], [673], [689], [636], [473], [674], [], [], [706], [], [], [], [], [], [], [], [], [718], [608], [], [], [], [172], [], [], [837], [], [], [756], [], [756], [
    126], [], [], [], [], [538], [6], [], [737], [], [], [383], [], [], [], [898], [], [426], [636], [], [], [], [], [], [], [54], [573], [], [], [534], [], [], [], [783], [940], [377], [], [], [565], [586], [], [], [], [], [], [], [], [], [], [63], []]

rst = [None, -1, -1, -1, -1, -1, -1, -1, None, 450, -1, -1, None, 717, None, None, 717, 717, 567, None, None, None, None, None, 383, 673, None, 689, 706, 706, 706, 706, 636, 706, 473, None, None, 674, 706, 718, None, 608, 608, None, 172, 837, None, 756, None, None,
       756, 756, 126, 126, None, None, 538, None, 6, 737, None, 737, 737, 737, None, 383, None, None, 898, 898, 898, 898, 636, 426, None, None, 636, 573, None, 54, 573, 534, None, None, None, 940, 783, None, None, 940, 940, 940, 377, 586, 565, 586, 586, -1, None, 63]
for i in xrange(1, len(func_list), 1):
    func = func_map[func_list[i]]
    if arg_list[i]:
        tmp = func(arg_list[i])
    else:
        tmp = func()
    # rst.append(tmp)
    if isinstance(tmp, list):
        tmp = tmp[0]
    if rst[i] != tmp:
        print func_list[i], arg_list[i], tmp, i
print rst
