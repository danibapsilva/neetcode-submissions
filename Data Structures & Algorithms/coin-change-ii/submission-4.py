class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]
        return dp[-1]

        # dp[a] represents the number of ways we can add up to amount a.
        # For every coin, we check every amount from that coin up to the target.
        # dp[a - c] represents the number of ways to make the remaining amount
        # after using coin c, so we add those ways to dp[a].
        # dp[0] = 1 because there is exactly one way to make amount 0: use no coins.
        # We process coins one at a time so that different orders of the same
        # coins are not counted as different combinations.
        # After processing every coin, dp[amount] is the total number of combinations.