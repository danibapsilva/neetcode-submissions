class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        nums.sort()
        def backtrack(start):
            res.append(subset.copy())
            for child in range(start, len(nums)):
                if child > start and nums[child] == nums[child - 1]:
                    continue
                
                subset.append(nums[child])
                backtrack(child + 1)
                subset.pop()
        
        backtrack(0)
        return res