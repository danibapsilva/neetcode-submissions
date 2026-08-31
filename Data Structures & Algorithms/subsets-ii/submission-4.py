class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n, subset, res = len(nums), [], []
        nums.sort()

        def backtrack(start: int) -> None:
            res.append(subset.copy())
            
            for child in range(start, n):
                if child > start and nums[child] == nums[child - 1]:
                    continue
                subset.append(nums[child])
                backtrack(child + 1)
                subset.pop()
        
        backtrack(0)
        return res