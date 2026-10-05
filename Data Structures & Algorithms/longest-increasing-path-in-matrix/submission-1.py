class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        DIRECTIONS = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        
        def dfs(r: int, c: int, prevVal: int) -> int:
            if (
                not 0 <= r < ROWS or
                not 0 <= c < COLS or
                matrix[r][c] <= prevVal
            ):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = 1
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                res = max(res, 1 + dfs(nr, nc, matrix[r][c]))
                dp[(r, c)] = res
                
            return res

        LIP = 0
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, dfs(r, c, float("-inf")))
        return LIP
