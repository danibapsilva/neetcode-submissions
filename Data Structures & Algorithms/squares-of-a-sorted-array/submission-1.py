class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        res_indx = n - 1
        l, r = 0, n - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[res_indx] = nums[l]**2
                l += 1
            else:
                res[res_indx] = nums[r]**2
                r -= 1
            res_indx -= 1
        
        return res