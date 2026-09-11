class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(grid), len(grid[0])
        FRESH, ROTTEN = 1, 2

        q = deque()
        freshCount = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN:
                    q.append((r, c))
                elif grid[r][c] == FRESH:
                    freshCount += 1
        

        minutes = 0
        while q and freshCount:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if (
                        not 0 <= nr < ROWS or
                        not 0 <= nc < COLS or
                        grid[nr][nc] != FRESH
                    ):
                        continue
                    
                    freshCount -= 1
                    grid[nr][nc] = ROTTEN
                    q.append((nr, nc))
            minutes += 1
            
        return minutes if not freshCount else -1