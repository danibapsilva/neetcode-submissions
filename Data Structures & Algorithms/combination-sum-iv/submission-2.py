class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        res = 0
        dp = {}
        def backtrack(curr: int) -> int:
            if curr == target:
                return 1
            if curr in dp:
                return dp[curr]
            
            res = 0
            for num in nums:
                if num + curr > target:
                    break
                res += backtrack(curr + num)
            dp[curr] = res
            return res
        
        return backtrack(0)
            