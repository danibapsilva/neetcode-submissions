class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n, res, combination = len(candidates), [], []
        candidates.sort()

        def backtrack(curr: int, start: int) -> None:
            if curr == target:
                res.append(combination.copy())
                return
            
            for child in range(start, n):
                if child > start and candidates[child] == candidates[child - 1]:
                    continue
                if curr + candidates[child] > target:
                    continue
                
                curr += candidates[child]
                combination.append(candidates[child])

                backtrack(curr, child + 1)

                curr -= candidates[child]
                combination.pop()
        
        backtrack(0, 0)
        return res