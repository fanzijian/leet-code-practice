#!/usr/bin/env python
#-*- coding: utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        for i in range(len(nums)):
            if i < 2:
                n += 1
                continue
            if nums[i] > nums[n - 2]:
                nums[n] = nums[i]
                n += 1
        print nums
        return n

        if len(nums) <= 2:
            return len(nums)
        n = 0 # 指向当前位置
        m = 0 # 连续重复次数
        for i in range(len(nums)):
            # print i, n, m, nums
            # 更新m
            if i == 0:
                continue
            if nums[i] == nums[i - 1]:
                m += 1
            else:
                m = 0
            # 当前值与最新值相等，且重复2次以内，则长度增加
            if nums[n] == nums[i]:
                if m < 2:
                    n += 1
                    nums[n] = nums[i]
            else:
                # 当当前值与最新值不等时，说明需要更新
                n = n + 1
                nums[n] = nums[i]
                m = 0
        # print nums
        return n + 1


obj = Solution()
print "============"
# print obj.removeDuplicates([0, 1, 1])
# print "============"
# print obj.removeDuplicates([0, 0, 1])
# print "============"
# print obj.removeDuplicates([1, 1, 1, 2, 2, 3])
# print "============"
print obj.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
