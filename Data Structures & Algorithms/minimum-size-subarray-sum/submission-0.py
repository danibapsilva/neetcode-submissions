class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        minS, l, curr = float("inf"), 0, 0
        for r in range(n):
            curr += nums[r]
            while curr >= target:
                minS = min(minS, r - l + 1)
                curr -= nums[l]
                l += 1
        return minS if minS != float("inf") else 0