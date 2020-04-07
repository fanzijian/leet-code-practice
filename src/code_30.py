#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # 窗口大小，单词对应的长度
        m = 0
        interval = len(words[0])
        hash_map = {}

        # 数据准备，建立待检索的map
        for w in words:
            m += len(w)
            if w not in hash_map:
                hash_map[w] = 0
            hash_map[w] += 1

        # 待遍历字符长度
        n = len(s)
        # 过滤掉异常情况
        if m > n:
            return []
        # 遍历滑动窗口处理
        rst = []
        for i in xrange(0, n, 1):
            # 判断当前[i, i+m]是否是目标字符串
            flag = self.check_target(s[i:i+m], hash_map, interval)
            if flag:
                rst.append(i)
                print s[i:i+m]
        return rst

    def check_target(self, s, hash_map, interval):
        rst = {}
        for i in xrange(0, len(s), interval):
            w = s[i:i+ interval]
            if w in hash_map:
                if w not in rst:
                    rst[w] = 0
                rst[w] += 1
                if rst[w] <= hash_map[w]:
                    continue
            return False
        for w in hash_map:
            if w in rst and hash_map[w] == rst[w]:
                continue
            return False
        return True

obj = Solution()
print obj.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"])
# print obj.check_target('goodbestword', {"word": 2, "good": 1, "best": 1}, 4)
