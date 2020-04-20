#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
快排

Authors: fanzijian
Date:    2020-04-19 13:46:56

"""
class SortSolution(object):
    def __init__(self):
        pass


    def quick_sort(self, data):
        """[重构数组的快排]
        """
        N = len(data)
        if N < 2:
            return data
        mid = data[ N // 2]
        data.remove(mid)
        r_list = []
        l_list = []
        for val in data:
            if val > mid:
                r_list.append(val)
            else:
                l_list.append(val)
        print l_list, r_list
        return self.quick_sort(l_list) + [mid] + self.quick_sort(r_list)

    def quick_sort2(self, l, r, data):
        """[原地排序]
        """
        # 选择基准
        if l >= r:
            return

        stand = data[r]
        i = l - 1
        # 遍历，将大于等于基准值的放在右边边，小于的放在左边
        for j in xrange(l, r, 1):
            if data[j] <= stand:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i+1], data[r] = data[r], data[i+1]
        self.quick_sort2(l, i-1, data)
        self.quick_sort2(i+1, r, data)


if __name__ == "__main__":
    obj = SortSolution()
    nums = [1, 3, 9, 4, 2, 5, 0]
    obj.quick_sort2(0, len(nums)-1, nums)
    print nums
