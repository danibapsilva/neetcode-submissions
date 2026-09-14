class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxS, curr = nums[0],  0
        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            maxS = max(maxS, curr)
        return maxS