class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1
        return -1