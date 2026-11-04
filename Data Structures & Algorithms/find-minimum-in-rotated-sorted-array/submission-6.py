class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        l, r = 0, n -1
        while l < r:
            middle = l + (r - l) // 2
            
            if nums[r] < nums[middle]:
                l = middle + 1
            else:
                r = middle
        
        return nums[r]