class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for indx, num in enumerate(nums):
            need = target - num
            if need in prev:
                return [prev[need], indx]
            prev[num] = indx
        return []