class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(heights), len(heights[0])
        visited = set()

        heap = [[0, 0, 0]] # diff, row, col
        while heap:
            diff, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue

            if r == ROWS - 1 and c == COLS - 1:
                return diff

            visited.add((r, c))

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if (
                    not 0 <= nr < ROWS or
                    not 0 <= nc < COLS or
                    (nr, nc) in visited
                ):
                    continue
                ndiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(heap, [ndiff, nr, nc])

        return 0
