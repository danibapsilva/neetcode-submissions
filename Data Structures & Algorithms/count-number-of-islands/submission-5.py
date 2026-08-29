class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if (
                min(r, c) < 0
                or r >= ROWS or c >= COLS
                or grid[r][c] != '1'
            ):
                return
            
            grid[r][c] = '0'
            for nr, nc in DIRECTIONS:
                dfs(r + nr, c + nc)
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        
        return islands