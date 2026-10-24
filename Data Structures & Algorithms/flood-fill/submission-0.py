class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(image), len(image[0])
        
        original = image[sr][sc]
        if original == color:
            return image

        def dfs(r: int, c: int) -> None:
            if (
                not 0 <= r < ROWS or
                not 0 <= c < COLS or
                image[r][c] != original
            ):
                return

            image[r][c] = color
            for dr, dc in DIRECTIONS:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)
        
        dfs(sr, sc)
        return image