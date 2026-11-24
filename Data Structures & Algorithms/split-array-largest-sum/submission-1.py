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
    

    # essentially the maximum range it could be is the total sum of nums,
    # and the minimum range is the largest value in nums (if len(sub) = 1)
    # we binary search the range between those two values, and we deem it
    # possible to split from the currently searched/middle value, if canSplit
    # is true. canSplit is a greedy algo that simply counts wether we can
    # make enough subarrays that are within the middle value, and if we have
    # to make too many subarrays, we return False, but if we make exactly the
    # right amount of subarrays we return True, and we can return True if the
    # value is less subarrays because we know that we can always just further
    # split one subarray into two smaller ones, meeting the number k.