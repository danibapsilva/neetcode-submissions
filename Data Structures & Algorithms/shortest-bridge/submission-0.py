class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS = COLS = len(grid)
        WATER, LAND, VISITED = 0, 1, 2
        
        q1, q2, islandFound = deque(), deque(), False
        for r in range(ROWS):
            if islandFound:
                break
            for c in range(COLS):
                if grid[r][c] == LAND:
                    islandFound = True
                    
                    grid[r][c] = VISITED
                    q1.append((r, c))
                    while q1:
                        row, col = q1.popleft()
                        q2.append((row, col))
                        for dr, dc in DIRECTIONS:
                            nr, nc = row + dr, col + dc
                            if (
                                not 0 <= nr < ROWS or
                                not 0 <= nc < COLS or
                                grid[nr][nc] != LAND
                            ):
                                continue
                            grid[nr][nc] = VISITED
                            q1.append((nr, nc))
                    break
        
        res = 0
        while q2:
            for _ in range(len(q2)):
                row, col = q2.popleft()
                for dr, dc in DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if (
                        not 0 <= nr < ROWS or
                        not 0 <= nc < COLS or
                        grid[nr][nc] == VISITED # Visited this time to search for island
                    ):
                        continue
                    
                    if grid[nr][nc] == LAND:
                        return res # Other island found, with 1's not visited
                    
                    grid[nr][nc] = VISITED
                    q2.append((nr, nc))
            res += 1

        return res
