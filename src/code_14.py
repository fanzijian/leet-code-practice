#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        common_prefix = ""
        j = 0
        while True:
            tmp = ''
            for i in range(len(strs)):
                if len(strs[i]) <= j:
                    return common_prefix
                if tmp == '':
                    tmp = strs[i][j]
                else:
                    if tmp != strs[i][j]:
                        return common_prefix
            common_prefix += tmp
            j += 1
