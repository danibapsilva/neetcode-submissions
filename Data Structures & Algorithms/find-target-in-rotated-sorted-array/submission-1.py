class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = l + (r - l) // 2

            if nums[middle] == target:
                return middle
            
            if nums[middle] >= nums[r]:
                if nums[middle] < target or target <= nums[r]:
                    l = middle + 1
                else:
                    r = middle - 1
            else: # r > middle
                if nums[middle] < target <= nums[r]:
                    l = middle + 1
                else:
                    r = middle - 1
        return -1