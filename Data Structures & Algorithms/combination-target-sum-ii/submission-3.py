class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, combination = [], []

        candidates.sort()
        def backtrack(start, curr):
            if curr == target:
                res.append(combination.copy())
                return

            for child in range(start, len(candidates)):
                if child > start and candidates[child] == candidates[child - 1]:
                    continue
                if curr + candidates[child] > target:
                    continue
                combination.append(candidates[child])
                backtrack(child + 1, curr + candidates[child])
                combination.pop()
        
        backtrack(0, 0)
        return res