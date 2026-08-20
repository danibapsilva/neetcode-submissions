class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, comb = [], []

        def backtrack(curr, start):
            if curr == target:
                res.append(comb.copy())
                return
            
            for i in range(start, len(nums)):
                if curr + nums[i] > target:
                    continue
                
                curr += nums[i]
                comb.append(nums[i])

                backtrack(curr, i)

                curr -= nums[i]
                comb.pop()
        
        backtrack(0, 0)
        return res