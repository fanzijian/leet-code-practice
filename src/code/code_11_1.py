#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Solution(object):
    """[该方法超时，废弃]
    耗时分析，sorted这一步，耗时导致变成了O(n^2),因此导致了超时
    """
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 遍历数组，整理结果成map 值-index映射关系
        # 遍历整理后的map，从最大开始，依次计算不同级别的最大容量（计算底级别的时候，需要把高级别的加上）
        height_map = {}
        max_area = 0
        for i in range(len(height)):
            if height[i] not in height_map:
                height_map[height[i]] = []
            height_map[height[i]].append(i)
        height_list = sorted(height_map.keys(), reverse=True)
        index_list = []
        for i in range(len(height_list)):
            index_list += height_map[height_list[i]]
            tmp_area = (max(index_list) - min(index_list)) * height_list[i]
            if tmp_area > max_area:
                print index_list, height_list[i]
                max_area = tmp_area
        return max_area

obj = Solution()
print obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
