class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if not matrix[r][c]:
                    for i in range(ROWS):
                        if matrix[i][c] != 0:
                            matrix[i][c] = float("inf")

                    for j in range(COLS):
                        if matrix[r][j] != 0:
                            matrix[r][j] = float("inf")

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == float("inf"):
                    matrix[r][c] = 0
