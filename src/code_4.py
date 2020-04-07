#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 获取两个队列的中位数，对比大小，保障在较大的队列的右边以及较小队列的左边同时减去同样的数量
        # 递归下去，最终就可以得到结果
        # 需要考虑好终止条件，因为最后的2个结果中，可能会参与比较
        # print nums1, nums2
        if len(nums1) <= 4 or len(nums2) <= 4:
            # 当其中有一个长度小于等于2时，就可以直接得到结果了
            # 则中位数为该队列2个+上另外队列的中间4个数字共6个的中位数
            # 将最长的队列缩短
            if len(nums1) > 2:
                nums1 = self.resize_list(nums1)

            if len(nums2) > 2:
                nums2 = self.resize_list(nums2)
            print nums1, nums2

            nums = nums1 + nums2
            while(len(nums) > 4):
                _min = min(nums)
                _max = max(nums)
                nums.pop(nums.index(_min))
                nums.pop(nums.index(_max))
            nums1 = nums
            nums2 = []
            print nums1, nums2
        total = len(nums1) + len(nums2)

        if total in [1, 2]:
            return float(sum(nums1) + sum(nums2)) / total
        # if len(nums1) + len(nums2) == 3:
        #     return sum(nums1) + sum(nums2) - max(nums1 + nums2) - min(nums1 + nums2)
        if total in [3, 4]:
            return (float(sum(nums1)) + sum(nums2) - max(nums1 + nums2) - min(nums1 + nums2))/ (total - 2)

        rst_1 = self.getMidOfOneSortedArray(nums1)
        rst_2 = self.getMidOfOneSortedArray(nums2)
        if rst_1[1] == rst_2[1]:
            return rst_1[1]
        else:
            # 比较中间值大小，使得队列1为中位数较小的队列
            if rst_1[1] > rst_2[1]:
                rst_1, rst_2 = self.swap_list(rst_1, rst_2)
                nums1, nums2 = self.swap_list(nums1, nums2)
            print rst_1, rst_2, nums1, nums2
            count = min(rst_1[0], rst_2[0])
            nums1 = nums1[count:] if rst_1[2] else nums1[:-count]
            nums2 = nums2[:-count] if rst_2[2] else nums2[count:]
            print count, nums1, nums2
            return self.findMedianSortedArrays(nums1, nums2)

    def getMidOfOneSortedArray(self, nums):
        """[获取队列的中位数，index]
        :type nums: List[int]
        :rtype: list
        """
        length = len(nums)
        mid = 0
        index = length / 2
        if length % 2 == 0:
            mid = (float(nums[index]) + nums[index-1]) / 2
        else:
            mid = nums[index]
        return index, mid, nums[0] <= nums[-1]

    def swap_list(self, nums1, nums2):
        tmp = nums1
        nums1 = nums2
        nums2 = tmp
        return nums1, nums2

    def resize_list(self, nums):
        length = len(nums)
        if length <= 4:
            return nums
        if length % 2 == 0:
            return nums[length/2 - 2: length/2 + 2]
        else:
            return nums[length/2 - 1: length/2 +2]

nums1 = [2,2,2,2]
nums2 = [2,2,2]

obj = Solution()

print obj.findMedianSortedArrays(nums1, nums2)
