class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxL = 0
        for num in numsSet:
            if num - 1 not in numsSet: # beg seq
                length = 1
                while num + length in numsSet:
                    length += 1
                maxL = max(maxL, length)
        return maxL