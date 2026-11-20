class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.binarySearch(nums, target, True)
        end   = self.binarySearch(nums, target, False)
        return [start, end]
    
    def binarySearch(self, nums: List[int], target: int, leftBias: bool) -> int:
        n = len(nums)

        l, r = 0, n - 1
        res = -1
        while l <= r:
            middle = l + (r - l) // 2
            if nums[middle] == target:
                res = middle
                if leftBias:
                    r = middle - 1
                else:
                    l = middle + 1
            elif nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1

        return res