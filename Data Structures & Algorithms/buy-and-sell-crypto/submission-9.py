class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = maxP = 0
        for r in range(1, len(prices)):
            maxP = max(maxP, prices[r] - prices[l])
            while prices[l] > prices[r]:
                l += 1
        return maxP