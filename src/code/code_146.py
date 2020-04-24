#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
题目链接：https://leetcode-cn.com/problems/lru-cache/

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

思路：

目前的算法，用了remove操作，是O(N)的，所以优化的话，
需要维护相应的关系，使得O(1)能够找到
可以维护一个双向链表，用于维护新旧关系

Authors: fanzijian
Date:    2020-04-06 11:23:56

"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.key_queue = []
        self.size = 0


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        # 更新索引时间
        self.key_queue.remove(key)
        self.key_queue.append(key)
        return self.cache[key]["val"]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            self.size += 1
            if self.size > self.capacity:
                # 删除最旧的
                key_to_del = self.key_queue[0]
                self.key_queue = self.key_queue[1:]
                del self.cache[key_to_del]
            # 增加
            self.cache[key] = {"val": value}
            self.key_queue.append(key)
        else:
            self.cache[key] = {"val": value}
            self.key_queue.remove(key)
            self.key_queue.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
