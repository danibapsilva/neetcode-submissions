class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(grid), len(grid[0])
        WATER, LAND = 0, 1

        perim = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND:
                    for dr, dc in DIRECTIONS:
                        nr, nc = r + dr, c + dc
                        if (
                            not 0 <= nr < ROWS or
                            not 0 <= nc < COLS or
                            grid[nr][nc] != LAND
                        ):
                            perim += 1
        return perim