class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = count = 0
        for num in nums:
            if not count:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate