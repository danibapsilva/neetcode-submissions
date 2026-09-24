class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        r, c, dr, dc = 0, 0, 0, 1
        for counter in range(n * n):
            if (
                not 0 <= r + dr < n or
                not 0 <= c + dc < n or
                matrix[r + dr][c + dc] != 0
            ):
                dr, dc = dc, -dr
            
            matrix[r][c] = counter + 1
            r, c = r + dr, c + dc
        return matrix