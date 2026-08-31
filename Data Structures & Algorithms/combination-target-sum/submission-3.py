class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n, res, combination = len(nums), [], []

        def backtrack(curr: int, start: int) -> None:
            if curr == target:
                res.append(combination.copy())
                return
            
            for child in range(start, n):
                if nums[child] + curr > target:
                    continue
                
                curr += nums[child]
                combination.append(nums[child])

                backtrack(curr, child)

                curr -= nums[child]
                combination.pop()
        
        backtrack(0, 0)
        return res