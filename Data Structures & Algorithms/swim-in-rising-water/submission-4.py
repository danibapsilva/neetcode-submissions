class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(grid), len(grid[0])

        heap = [(grid[0][0], (0, 0))]
        visited = set()

        while heap:
            time, (r, c) = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == ROWS - 1 and c == COLS - 1:
                return time

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if (
                    not 0 <= nr < ROWS or
                    not 0 <= nc < COLS or
                    (nr, nc) in visited
                ):
                    continue
                new_time = max(time, grid[nr][nc])
                heapq.heappush(heap, (new_time, (nr, nc)))

        return -1