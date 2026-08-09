class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numset = set()

        for num in nums:
            if num in numset:
                return num
            numset.add(num)