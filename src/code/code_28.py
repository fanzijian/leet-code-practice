#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
问题: 存在目标字符串a，模式字符串b，快速查找b在a中出现的位置
参考题目：https://leetcode-cn.com/problems/implement-strstr/

原始思路，维护一个长度为len(b)的滑动窗口，每次滑动一个，然后对比，由于每次都是全量比，对导致极端情况下，每个字符都要比len(b)次

kmp则是利用当前已经对比得到的结果，当发现不匹配时，利用已知的结果判断下一次滑动的步长
例如，a='abcabcad', b='abcad',当匹配到'abca',第五个'd'不匹配，那么接下来该滑动多少呢？
即已经匹配的'abca'，尾部开始的后缀和头部开始的前缀有存在重合的'a'子串，那么表示存在复用的可能，则移动到字符串b中的第一个'a'与
目标字符串对齐即可，以此类推

kmp算法实现:
1. 因为模式串是已知的，因此针对模式字符串生成next队列，该队列维护了当匹配失败后，下一次的启动点的位置
2. 移动滑动窗口，当发生不匹配时，则根据next队列，计算滑动步数 next(char) + 1


Authors: fanzijian
Date:    2020-04-12 11:23:56

"""

class Solution(object):
    def next(self, b):
        rst = [-1 for i in range(len(b))]
        k = -1
        for i in xrange(1, len(b), 1):
            while k > -1 and b[i] != b[k+1]:
                k = rst[k]
            if b[i] == b[k+1]:
                k += 1
            rst[i] = k
        return rst

    def getSubStrPosition(self, a, b):
        N = len(a)
        M = len(b)
        j = 0
        rst = self.next(b)
        print rst
        for i in xrange(0, N, 1):
            while j > 0 and a[i] != b[j]:
                j = rst[j-1] + 1
            if a[i] == b[j]:
                j += 1
            if j == M:
                return i - M + 1
        return -1

obj = Solution()
print obj.getSubStrPosition('', '')


