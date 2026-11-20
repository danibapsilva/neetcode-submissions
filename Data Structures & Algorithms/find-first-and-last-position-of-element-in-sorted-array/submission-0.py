class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            middle = l + (r - l) // 2
            if nums[middle] == target:
                start = end = middle
                while start > 0 and nums[start - 1] == target:
                    start -= 1
                while end < n - 1 and nums[end + 1] == target:
                    end += 1
                return [start, end]
            elif nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1
        

        return [-1, -1]