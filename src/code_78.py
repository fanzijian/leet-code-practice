class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = [[]]
        for i in xrange(0, len(nums), 1):
            num = nums[i]
            tmp = []
            for sub in rst:
                tmp.append(sub + [num])
            rst += tmp
            print rst
        return rst

obj = Solution()
print obj.subsets([1,2,3])