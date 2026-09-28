class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = {}
        def dfs(i: int, buying: bool) -> int:
            if i >= n:
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                bought = dfs(i + 1, False) - prices[i]
                skip = dfs(i + 1, True)
                dp[(i, buying)] = max(bought, skip)
            else:
                sold = dfs(i + 2, True) + prices[i]
                skip = dfs(i + 1, False)
                dp[(i, buying)] = max(sold, skip)
            return dp[(i, buying)]
        
        return dfs(0, True)