class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        total = 0
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if matrix[r][c]:
                    dp[r][c] = 1 + min(dp[r][c + 1], dp[r + 1][c], dp[r + 1][c + 1])
                    total += dp[r][c]
        return total