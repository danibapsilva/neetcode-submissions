class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, combination = [], []

        def backtrack(start, curr):
            if curr == target:
                res.append(combination.copy())
                return

            for child in range(start, len(nums)):
                if curr + nums[child] > target:
                    continue
                combination.append(nums[child])
                backtrack(child, curr + nums[child])
                combination.pop()
        
        backtrack(0, 0)
        return res