class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1): # for every amount possibility in amounts
            for c in coins: # for every coin at our disposal
                if a - c >= 0: # if curr amount - curr coin could have subproblem
                    dp[a] = min(dp[a], dp[a - c] + 1)
                    # set amnt of coins to solve amount to min of found vs existing
        return dp[-1] if dp[-1] != float("inf") else -1

        # set the initital dp array with a large/infinite value (like amount+1)
        # and set the 0th index to have 0 possibilites (takes 0 coins for amount 0)
        # then iterate for every amount from 1 to target amount and check all the
        # coin possiblities that we have available to us, for every coin we check
        # wether we have already solved a subproblem/step below that coin
        # the step below that coin is defined as the current amount we are checking
        # minus the current coin at our disposal, and if we check the dp arr
        # and amount - coin is already solved (solved meaning we know min amount of
        # coins it takes to get that amount), we add 1 coin for current coin, and set
        # dp[a] to the minimum of what we found and its existing value
