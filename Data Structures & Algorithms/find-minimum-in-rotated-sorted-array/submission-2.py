class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            middle = l + (r - l) // 2
            res = min(res, nums[middle])
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle - 1
            
        return res
        