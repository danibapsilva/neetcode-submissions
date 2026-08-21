class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero = one = two = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[two], nums[one], nums[zero] = 2, 1, 0
                two += 1
                one += 1
                zero += 1
            elif nums[i] == 1:
                nums[two], nums[one] = 2, 1
                two += 1
                one += 1
            else:
                nums[two] = 2
                two += 1
    