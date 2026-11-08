class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []
        for indx, a in enumerate(nums):
            if a > 0:
                break
            if indx >= 1 and a == nums[indx - 1]:
                continue
            
            l, r = indx + 1, n - 1
            while l < r:
                ts = a + nums[l] + nums[r]
                if not ts:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif ts > 0:
                    r -= 1
                else:
                    l += 1
        return res
                    
            