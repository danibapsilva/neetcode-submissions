class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, permutation = [], []

        n = len(nums)
        used = [False] * n

        def backtrack():
            if len(permutation) == n:
                res.append(permutation.copy())
                return
            
            for child in range(n):
                if not used[child]:
                    used[child] = True
                    permutation.append(nums[child])

                    backtrack()

                    used[child] = False
                    permutation.pop()
        
        backtrack()
        return res