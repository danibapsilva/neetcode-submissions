class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[n - 1][m - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if obstacleGrid[i][j]:
                    continue
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0] if not obstacleGrid[-1][-1] else 0