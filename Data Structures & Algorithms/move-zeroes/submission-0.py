class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        free = 0
        for indx, num in enumerate(nums):
            if num:
                nums[indx], nums[free] = nums[free], nums[indx]
                free += 1
        
                