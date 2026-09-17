class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        maxS = 0
        for num in numset:
            if num - 1 in numset:
                continue
            length = 1
            while num + length in numset:
                length += 1
            maxS = max(maxS, length)
        return maxS