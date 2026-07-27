class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (l + r) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r -= 1
            else:
                l += 1
        
        return -1