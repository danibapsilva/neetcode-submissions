class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c]:
                    q.append((r, c))
        

        while q:
            row, col = q.popleft()
            for dr, dc in DIRECTIONS:
                nr, nc = row + dr, col + dc
                if (
                    min(nr, nc) < 0
                    or nr >= ROWS
                    or nc >= COLS
                    or grid[nr][nc] != INF
                 ):
                    continue

                grid[nr][nc] = grid[row][col] + 1
                q.append((nr, nc))