class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posDiag, negDiag = set(), set(), set()

        res, positions = [], []
        def backtrack(row: int) -> None:
            if row == n:
                res.append(positions.copy())
                return

            for col in range(n):
                if col in cols or col + row in posDiag or col - row in negDiag:
                    continue
                
                placement = '.' * n
                placement = placement[:col] + 'Q' + placement[col + 1:]
                
                cols.add(col)
                posDiag.add(col + row)
                negDiag.add(col - row)
                positions.append(placement)

                backtrack(row + 1)

                cols.remove(col)
                posDiag.remove(col + row)
                negDiag.remove(col - row)
                positions.pop()

        backtrack(0)
        return res