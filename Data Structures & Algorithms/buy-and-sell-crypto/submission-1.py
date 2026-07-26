class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high, profit = prices[0], 0, 0
        for price in prices:
            if price < low:
                low = price
                high = 0
            elif price > high:
                high = price
                if high - low > profit:
                    profit = high - low
        return profit