class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp

        return dp[target]

        # dp[i] represents the amount of ways we can sum up to the total of i
        # so returning dp[target] returns amount of ways to sum up to target
        # all we need to keep track of is the previous element/index calculations
        # and we add or subtract the current/next element to each calculation/item

        # TRACE:
        # 0: 1
        # first {0: 1} -> VAL 2 -> 2: 1 & -2: 1
        # second {-2: 1, 2: 1} -> VAL 2 -> 4: 1, 0: 1, 0: 1, -4: 1
        # third {-4: 1, 0: 2, 4: 1} -> VAL 2 -> -2: 1, -6: 1, 2: 2, -2: 1, 6: 1, 2: 1
        # finish {-6: 1, -2: 1, 2: 3, 6: 1}
        # dp[target] = dp[2] = 3
