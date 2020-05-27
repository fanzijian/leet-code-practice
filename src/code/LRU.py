class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LRU(object):
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.idx_map = {}
        slave = Node(-1)
        self.head = slave
        self.tail = slave

    def get(self, key):
        if key in self.idx_map:
            cur = self.idx_map[key]
            self.move_node_to_end(cur)
            return cur.val
        else:
            return None

    def put(self, key, value):
        if self.size <= 0:
            return

        if key not in self.idx_map:
            node = Node(value)
            if self.count < self.size:
                if self.count == 0:
                    self.head.next = node
                    node.prev = self.head
                    self.head = node
                    self.tail = node
                else:
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                self.count += 1
                self.idx_map[key] = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                prev = self.head.prev
                prev.next = self.head.next
                self.head = self.head.next
                self.head.prev = prev
        else:
            cur = self.idx_map[key]
            self.move_node_to_end(cur)



    def move_node_to_end(self, cur):
        prev = cur.prev
        prev.next = cur.next
        cur.next.prev = prev
        self.tail.next = cur
        cur.prev = self.tail
        self.tail = cur
        cur.next = None

