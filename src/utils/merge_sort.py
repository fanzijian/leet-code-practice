#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
归并排序

Authors: fanzijian
Date:    2020-04-21 20:46:56

"""
class MergeSort(object):
    def __init__(self):
        pass

    def sort(self, S):
        N = len(S)
        mid = N // 2
        if N < 2:
            return
        left = S[:mid]
        right = S[mid:]
        self.sort(left)
        self.sort(right)
        self.merge(left, right, S)
        return S

    def merge(self, left, right, S):
        M, N = len(left), len(right)
        total = len(S)
        i = j = 0

        while i + j < total:
            if j == N or (i < M and left[i] < right[j]):
                S[i+j] = left[i]
                i += 1
            else:
                S[i+j] = right[j]
                j += 1
        return S


if __name__ == "__main__":
    left = [6, 3,2,8,4]
    right = [1,5,9,7]
    S = left + right
    obj = MergeSort()
    print obj.sort(S)
