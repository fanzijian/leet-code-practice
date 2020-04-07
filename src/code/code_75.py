class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i0 = 0
        i = 0
        i2 = len(nums) - 1
        while i <= i2:
            print nums, i, i0, i2
            if nums[i] == 0:
                nums[i0], nums[i] = nums[i], nums[i0]
                i0 += 1
            elif nums[i] == 2:
                nums[i2], nums[i] = nums[i], nums[i2]
                i2 -= 1
                i -= 1
            i += 1
nums = [2,1,2]

obj = Solution()
obj.sortColors(nums)
print nums