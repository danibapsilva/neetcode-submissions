class Solution:
    def solve(self, board: List[List[str]]) -> None:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(board), len(board[0])
        LAND, WATER = 'O', 'X'

        safe = set()
        def dfs(r: int, c: int) -> None:
            safe.add((r, c))
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    (nr, nc) not in safe and
                    board[nr][nc] == LAND
                ):
                    dfs(nr, nc)

        for r in range(ROWS):
            for c in range(COLS):
                if (
                    board[r][c] == LAND and
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])
                ):
                    dfs(r, c)
            
        for r in range(ROWS):
            for c in range(COLS):
                if (
                    (r, c) not in safe
                    and board[r][c] == LAND 
                ):
                    board[r][c] = WATER