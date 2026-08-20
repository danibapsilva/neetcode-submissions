class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, comb = [], []
        candidates.sort()

        def backtrack(curr, start):
            if curr == target:
                res.append(comb.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if curr + candidates[i] > target:
                    return
                
                curr += candidates[i]
                comb.append(candidates[i])

                backtrack(curr, i + 1)

                curr -= candidates[i]
                comb.pop()
        
        backtrack(0, 0)
        return res