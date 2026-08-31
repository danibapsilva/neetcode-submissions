class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        picked, permutation, res = [False] * n, [], []

        def backtrack() -> None:
            if len(permutation) == n:
                res.append(permutation.copy())
                return
            
            for child in range(n):
                if not picked[child]:
                    picked[child] = True
                    permutation.append(nums[child])

                    backtrack()

                    picked[child] = False
                    permutation.pop()
                    

        backtrack()
        return res