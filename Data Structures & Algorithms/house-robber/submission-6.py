class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        one, two = nums[0], max(nums[0], nums[1])
        
        ### MODIFYING INPUT ###
        # for i in range(2, n):
        #     nums[i] = max(nums[i] + one, two)
        #     one = two
        #     two = nums[i]
        
        # return max(one, two)

        for i in range(2, n):
            temp = max(nums[i] + one, two)
            one = two
            two = temp
        return max(one, two)