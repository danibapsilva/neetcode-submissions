class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        
        return max(LIS)

        # dp[i] represents the LIS at index i
        # find dp[i] using an default val of 1, each number can be its own substring
        # and we check from i, to n, whether there is any number greater that num[i]
        # if yes, we set dp[i] to be the max of its current value, and the value of
        # the greater number just found + 1 since we are adding nums[1] to substring
        # then at the end, we simply return the max value found in our dp arr