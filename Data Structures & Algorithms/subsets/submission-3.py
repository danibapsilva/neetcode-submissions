class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def backtrack(start):
            res.append(subset.copy())
            for child in range(start, len(nums)):
                subset.append(nums[child])
                backtrack(child + 1)
                subset.pop()
        
        backtrack(0)
        return res