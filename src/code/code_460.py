class Node(object):
    def __init__(self, key, val, freq):
        self.val = val
        self.key = key
        self.freq = freq
        self.next = None
        self.prev = None


def print_map(freq_map):
    for key in freq_map:
        tmp = []
        node = freq_map[key]
        while node:
            tmp.append(str(node.key))
            node = node.next
        print "frep: %s, key_list: %s" % (key, ','.join(tmp))


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_map = {}
        self.freq_map = {}

    def _delete_node(self, node):
        parent = node.prev
        child = node.next
        freq = node.freq
        # 双向链表删空了
        if not parent and not child:
            # 删除该频率节点
            if freq in self.freq_map:
                del self.freq_map[freq]
        elif not parent:
            self.freq_map[freq] = child
            child.prev = None
        elif not child:
            parent.next = None
        else:
            parent.next = child
            child.prev = parent

    def _add_node(self, node, freq):
        if freq not in self.freq_map:
            self.freq_map[freq] = node
            node.prev = None
            node.next = None
        else:
            pre_node = self.freq_map[freq]
            self.freq_map[freq] = node
            node.prev = None
            node.next = pre_node
            pre_node.prev = node

    def _rebalance_min_freq(self, freq_del, freq_add):
        if freq_del == self.min_freq:
            self.min_freq = min(self.freq_map.keys())
        if freq_add == 1:
            self.min_freq = 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 缓存中存在，则在freq中增加1,且从双向链表中删除该节点，在freq+1链表中插入该点
        # print "before get", key
        # print_map(self.freq_map)
        if key in self.key_map:
            node = self.key_map[key]
            self._delete_node(node)
            node.freq += 1
            self._add_node(node, node.freq)
            self._rebalance_min_freq(node.freq-1, node.freq)
            # print "after get", key
            # print_map(self.freq_map)
            return node.val
        # 缓存中不在，则返回-1
        else:
            # print "after get", key
            # print_map(self.freq_map)
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 缓存中存在，则更新freq_map中频率+1
        # print "before put", key, value
        # print_map(self.freq_map)
        if key in self.key_map:
            node = self.key_map[key]
            self._delete_node(node)
            node.freq += 1
            node.val = value
            self._add_node(node, node.freq)
            self._rebalance_min_freq(node.freq-1, node.freq)
        # 缓存中不存在，
        else:
            # 容量已满，则删除最不常用的(min_freq对应的最近的key)
            if self.size >= self.capacity:
                if self.min_freq == 0:
                    return
                node = self.freq_map[self.min_freq]
                while node.next:
                    node = node.next
                self._delete_node(node)
                # print 'delete full', node.key
                if node.key in self.key_map:
                    del self.key_map[node.key]
            # 容量未满则直接增加1个节点，更新key_map， freq_map，且更新min_freq=1
            freq = 1
            node = Node(key, value, freq)
            self._add_node(node, 1)
            self.size += 1
            self.key_map[key] = node
            self._rebalance_min_freq(None, node.freq)
        # print "after put", key, value
        # print_map(self.freq_map)
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
