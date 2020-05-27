class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRU(object):
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.cache = {}
        slave = Node(-1, -1)
        self.head = slave
        self.tail = slave

    def get(self, key):
        if key in self.cache:
            cur = self.cache[key]
            self.move_node_to_end(cur)
            return cur.val
        else:
            return None

    def put(self, key, value):
        if self.size <= 0:
            return

        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
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
                self.cache[key] = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node

                del self.cache[self.head.key]

                prev = self.head.prev
                prev.next = self.head.next
                self.head = self.head.next
                self.head.prev = prev
        else:
            cur = self.cache[key]
            cur.val = value
            self.move_node_to_end(cur)

    def move_node_to_end(self, cur):
        prev = cur.prev
        prev.next = cur.next
        cur.next.prev = prev
        self.tail.next = cur
        cur.prev = self.tail
        self.tail = cur
        cur.next = None
