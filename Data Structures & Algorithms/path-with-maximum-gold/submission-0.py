class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(grid), len(grid[0])
        PROHIBITED = 0

        res = 0
        def backtrack(r: int, c: int, curr: int) -> None:
            nonlocal res

            gold = grid[r][c]
            curr += gold
            grid[r][c] = PROHIBITED
            
            res = max(res, curr)
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if (
                    not 0 <= nr < ROWS or
                    not 0 <= nc < COLS or
                    grid[nr][nc] == PROHIBITED
                ):
                    continue
                backtrack(nr, nc, curr)
            
            grid[r][c] = gold

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != PROHIBITED:
                    backtrack(r, c, 0)
        return res
