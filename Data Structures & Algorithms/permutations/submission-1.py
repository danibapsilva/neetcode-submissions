class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, perm, picked = [], [], [False] * n
        
        def backtrack():
            if len(perm) == n:
                res.append(perm.copy())
                return
            
            for i in range(n):
                if not picked[i]:
                    perm.append(nums[i])
                    picked[i] = True

                    backtrack()

                    perm.pop()
                    picked[i] = False

        backtrack()
        return res
