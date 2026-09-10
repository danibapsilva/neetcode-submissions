class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        for i in range(2, n):
            one, two = cost[i - 1], cost[i - 2]
            cost[i] += min(one, two)
        return min(cost[-1], cost[-2])
