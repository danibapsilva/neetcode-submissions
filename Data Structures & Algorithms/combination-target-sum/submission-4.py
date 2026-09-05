class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, combination = [], []

        def backtrack(start: int, curr: int) -> None:
            if curr == target:
                res.append(combination.copy())
                return
            
            for child in range(start, len(nums)):
                if nums[child] + curr > target:
                    continue
                
                curr += nums[child]
                combination.append(nums[child])
                backtrack(child, curr)

                curr -= nums[child]
                combination.pop()
        
        backtrack(0, 0)
        return res