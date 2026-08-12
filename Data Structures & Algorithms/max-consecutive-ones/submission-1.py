class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = length = 0

        for num in nums:
            length = length + 1 if num else 0
            maxLen = max(maxLen, length)
        
        return maxLen