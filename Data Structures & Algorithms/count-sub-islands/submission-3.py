class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(grid1), len(grid1[0])
        LAND, WATER = 1, 0

        def dfs(r: int, c: int):
            valid = True
            stack = [(r, c)]
            grid2[r][c] = WATER

            while stack:
                r, c = stack.pop()

                if grid1[r][c] == WATER:
                    valid = False

                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if (
                        not 0 <= nr < ROWS or
                        not 0 <= nc < COLS or
                        grid2[nr][nc] != LAND
                    ):
                        continue

                    grid2[nr][nc] = WATER
                    stack.append((nr, nc))

            return valid

        subIslands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == LAND:
                    subIslands += int(dfs(r, c))

        return subIslands