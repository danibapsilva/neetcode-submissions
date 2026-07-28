class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        currMin = float("inf")
        while l <= r:
            middle = l + (r - l) // 2
            
            currMin = min(currMin, nums[middle])
            if nums[l] > nums[r]:
                if nums[middle] > nums[r]:
                    l = middle + 1
                else:
                    l += 1
            else:
                if nums[middle] > nums[l]:
                    r = middle - 1
                else:
                    r -= 1
            
        return currMin
        