class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            middle = l + (r - l) // 2
            if middle < n - 1 and nums[middle] < nums[middle + 1]:
                l = middle + 1
            elif middle > 0 and nums[middle] < nums[middle - 1]:
                r = middle - 1
            else:
                return middle
        return -1