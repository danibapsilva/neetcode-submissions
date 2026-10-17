class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n, res, combination = len(nums), [], []

        def backtrack(curr: int, start: int) -> None:
            if curr == target:
                res.append(combination.copy())
                return
            
            for child in range(start, n):
                num = nums[child]
                if num + curr > target:
                    continue
                
                combination.append(num)
                backtrack(curr + num, child)
                combination.pop()
        
        backtrack(0, 0)
        return res