class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float("inf")] * n
        dp[src] = 0

        for i in range(k + 1):
            next_dp = dp.copy()
            for s, d, p in flights:
                if dp[s] == float("inf"):
                    continue
                path = dp[s] + p
                if path < next_dp[d]:
                    next_dp[d] = path
            dp = next_dp
        return dp[dst] if dp[dst] != float("inf") else -1