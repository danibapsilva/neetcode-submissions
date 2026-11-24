class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            middle = l + ((r - l) // 2)
            if self.canSplit(nums, k, middle):
                res = middle
                r = middle - 1
            else:
                l = middle + 1
        return res
    
    def canSplit(self, nums: List[int], k: int, largest: int) -> bool:
        curr, subarrays = 0, 1
        for num in nums:
            curr += num
            if curr > largest:
                subarrays += 1
                curr = num
        return subarrays <= k