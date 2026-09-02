class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(heights), len(heights[0])

        pacific, atlantic = set(), set()
        
        def dfs(r: int, c: int, visited: Set) -> None:
            visited.add((r, c))
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if (
                    (nr, nc) in visited
                    or min(nr, nc) < 0
                    or nr >= ROWS
                    or nc >= COLS
                    or heights[nr][nc] < heights[r][c]
                ):
                    continue
                dfs(nr, nc, visited)
            

        # pacific
        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)

        # atlantic
        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS - 1, atlantic)
        
        res = []
        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r, c])
        
        return res