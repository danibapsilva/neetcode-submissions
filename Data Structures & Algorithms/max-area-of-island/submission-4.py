class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIRECTIONS = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        ROWS, COLS = len(grid), len(grid[0])
        WATER, LAND = 0, 1

        def dfs(r: int, c: int) -> int:
            if (
                not 0 <= r < ROWS or
                not 0 <= c < COLS or
                grid[r][c] != LAND
            ):
                return 0
            
            grid[r][c] = WATER
            area = 1
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)
            return area

        maxA = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND:
                    maxA = max(maxA, dfs(r, c))
        return maxA