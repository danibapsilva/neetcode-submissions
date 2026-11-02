class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        first_row = first_col = False
        for r in range(ROWS):
            for c in range(COLS):
                if not matrix[r][c]:
                    if not r: first_row = True
                    if not c: first_col = True
                    matrix[r][0] = matrix[0][c] = 0
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if not matrix[r][0] or not matrix[0][c]:
                    matrix[r][c] = 0

        if first_row:
            for c in range(COLS):
                matrix[0][c] = 0
        if first_col:
            for r in range(ROWS):
                matrix[r][0] = 0