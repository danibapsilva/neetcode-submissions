class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = count = 0
        for num in nums:
            if not count:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate