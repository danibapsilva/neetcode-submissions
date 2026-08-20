class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, comb = [], []
        nums.sort()

        def backtrack(curr, start):
            if curr == target:
                res.append(comb.copy())
                return
            
            for i in range(start, len(nums)):
                if curr + nums[i] > target:
                    return
                
                comb.append(nums[i])
                curr += nums[i]

                backtrack(curr, i)

                popped = comb.pop()
                curr -= popped
        
        backtrack(0, 0)
        return res