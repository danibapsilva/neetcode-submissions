class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n, res, combination = len(candidates), [], []

        def backtrack(start: int, curr: int) -> None:
            if curr == target:
                res.append(combination.copy())
                return
            
            for child in range(start, n):
                num = candidates[child]
                if child > start and num == candidates[child - 1]:
                    continue
                
                if num + curr > target:
                    break
                
                combination.append(num)

                backtrack(child + 1, curr + num)

                combination.pop()

        backtrack(0, 0)
        return res