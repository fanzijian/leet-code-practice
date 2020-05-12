#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
各种排序

Authors: fanzijian
Date:    2020-5-12 11:46:56

"""
def quick_sort(nums):
    N = len(nums)
    if N < 2:
        return nums
    standard_value = nums[N-1]
    left = []
    mid = []
    right = []
    for i in xrange(0, N, 1):
        if nums[i] < standard_value:
            left.append(nums[i])
        elif nums[i] == standard_value:
            mid.append(nums[i])
        else:
            right.append(nums[i])
    left = quick_sort(left)
    right = quick_sort(right)
    return left + mid + right

def merge_sort(nums):
    def merge(list1, list2):
        rst = []
        N = len(list1)
        M = len(list2)
        i = j = 0
        while i < N and j < M:
            if list1[i] < list2[j]:
                rst.append(list1[i])
                i += 1
            else:
                rst.append(list2[j])
                j += 1
        if i < N:
            rst.extend(list1[i:])
        if j < M:
            rst.extend(list2[j:])
        return rst
    N = len(nums)
    if N < 2:
        return nums
    mid = N // 2
    left = nums[:mid]
    right = nums[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    nums = merge(left, right)
    return nums

def insert_sort(nums):
    N = len(nums)
    for i in xrange(1, N, 1):
        j = i
        while nums[j-1] > nums[j] and j > 0:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums

def heap_sort(nums):
    def heapify(heap, N, j):
        max_idx = j
        while True:
            if j * 2 <= N and heap[j*2] > heap[max_idx]:
                max_idx = j * 2
            if j * 2 + 1 <= N and heap[j*2+1] > heap[max_idx]:
                max_idx = j * 2 + 1
            heap[max_idx], heap[j] = heap[j], heap[max_idx]
            if j == max_idx:
                break
            j = max_idx

    heap = [0]
    heap.extend(nums)
    N = len(nums)
    m = N // 2
    for i in xrange(m, 0, -1):
        heapify(heap, N, i)
    for i in xrange(0, N, 1):
        heap[1], heap[N-i] = heap[N-i], heap[1]
        heapify(heap, N-i-1, 1)
    return heap[1:]

def select_sort(nums):
    N = len(nums)
    j = 0
    for j in xrange(0, N, 1):
        min_idx = N - 1
        for i in xrange(N, j, -1):
            if nums[i-1] < nums[min_idx]:
                min_idx = i - 1
        nums[min_idx], nums[j] = nums[j], nums[min_idx]
    return nums

if __name__ == "__main__":
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # nums = quick_sort(nums)
    # print nums
    print heap_sort(nums)
    # print quick_sort(nums)
