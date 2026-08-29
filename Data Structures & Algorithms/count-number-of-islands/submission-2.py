class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r: int, c: int) -> None:
            q = deque([(r, c)])
            grid[r][c] = '0'

            while q:
                row, col = q.popleft()

                for nr, nc in DIRECTIONS:
                    nr, nc = nr + row, nc + col
                    if (
                        min(nr, nc) < 0
                        or nr >= ROWS or nc >= COLS
                        or grid[nr][nc] != '1'
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = '0'

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        
        return islands