class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n, subset, res = len(nums), [], []

        def backtrack(start: int) -> None:
            res.append(subset.copy())
            
            for child in range(start, n):
                subset.append(nums[child])
                backtrack(child + 1)
                subset.pop()
        
        backtrack(0)
        return res