class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for num in nums:
            indx = abs(num)
            if nums[indx] < 0:
                return abs(num)
            
            nums[indx] *= -1
        
        return -1