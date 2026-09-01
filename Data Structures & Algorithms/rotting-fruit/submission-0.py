class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2

        freshCount = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                cell = grid[r][c]
                if cell == ROTTEN:
                    q.append((r, c))
                elif cell == FRESH:
                    freshCount += 1
        
        minutes = 0
        while q and freshCount:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if (
                        min(nr, nc) < 0
                        or nr >= ROWS
                        or nc >= COLS
                        or grid[nr][nc] != FRESH
                    ):
                        continue
                    
                    freshCount -= 1
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))
            minutes += 1
                

        return minutes if not freshCount else -1
