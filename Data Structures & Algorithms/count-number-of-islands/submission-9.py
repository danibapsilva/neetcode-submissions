class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(grid), len(grid[0])
        WATER, LAND = '0', '1'
        
        def dfs(r: int, c: int) -> None:

            grid[r][c] = WATER
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if (
                    not 0 <= nr < ROWS or
                    not 0 <= nc < COLS or
                    grid[nr][nc] != LAND
                ):
                    continue
                dfs(nr, nc)

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND:
                    dfs(r, c)
                    islands += 1
        return islands
