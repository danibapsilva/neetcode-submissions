class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(grid), len(grid[0])
        WATER, LAND = 0, 1

        visited = set()
        def dfs(r: int, c: int) -> int:
            if (
                not 0 <= r < ROWS or
                not 0 <= c < COLS or
                grid[r][c] != LAND
            ):
                return 1
            if (r, c) in visited:
                return 0
 
            visited.add((r, c))
            perim = 0
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                perim += dfs(nr, nc)
            return perim

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND:
                    return dfs(r, c)
        return 0