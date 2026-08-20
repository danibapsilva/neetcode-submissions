class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res, comb = [], []
        candidates.sort()

        def backtrack(curr, start):
            if curr == target:
                res.append(comb.copy())
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                added = candidates[i] + curr
                if added > target:
                    return

                comb.append(candidates[i])
                curr = added

                backtrack(curr, i + 1)

                comb.pop()
                curr -= candidates[i]
        
        backtrack(0, 0)
        return res