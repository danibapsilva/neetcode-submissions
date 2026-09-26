class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        r = l = 0
        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            if not farthest:
                return False
        return True