class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i: int) -> None:
            if i == len(nums):
                res.append(sol.copy())
                return
            
            # Dont add nums[i] - left branch
            backtrack(i + 1)

            # Add nums[i] - right branch
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        
        backtrack(0)
        return res