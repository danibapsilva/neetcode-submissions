class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numset = set(nums)
        n = len(nums)

        res = []
        for i in range(1, n + 1):
            if i not in numset:
                res.append(i)
        
        return res

