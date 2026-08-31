class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or grid[r][c] != 1
            ):
                return 0
            
            area = 1

            grid[r][c] = 0
            for nr, nc in DIRECTIONS:
                area += dfs(r + nr, c + nc)
            
            return area
    
        maxA = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxA = max(maxA, dfs(r, c))
        
        return maxA