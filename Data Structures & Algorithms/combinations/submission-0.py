class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, combination = [], []
        
        def backtrack(start: int) -> None:
            if len(combination) == k:
                res.append(combination.copy())
                return
            
            for child in range(start, n + 1):
                combination.append(child)
                backtrack(child + 1)
                combination.pop()
        
        backtrack(1)
        return res