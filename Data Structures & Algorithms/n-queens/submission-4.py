class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROWS = COLS = n
        cols, posDiags, negDiags = set(), set(), set()

        res, positions = [], []
        def backtrack(row: int):
            if row == ROWS:
                res.append(positions.copy())
                return
            for col in range(COLS):
                if col in cols or col + row in posDiags or col - row in negDiags:
                    continue
                placement = '.' * COLS
                placement = placement[:col] + 'Q' + placement[col + 1:]

                posDiags.add(col + row)
                negDiags.add(col - row)
                cols.add(col)
                positions.append(placement)

                backtrack(row + 1)

                posDiags.remove(col + row)
                negDiags.remove(col - row)
                cols.remove(col)
                positions.pop()
        
        backtrack(0)
        return res
                