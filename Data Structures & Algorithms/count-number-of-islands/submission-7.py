class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if (
                not 0 <= r < ROWS or
                not 0 <= c < COLS or
                grid[r][c] != "1"
            ):
                return
            grid[r][c] = "0"
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
                
        return islands