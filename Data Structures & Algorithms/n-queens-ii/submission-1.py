class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, posDiag, negDiag = set(), set(), set()

        res = 0
        def backtrack(row: int) -> None:
            nonlocal res

            if row == n:
                res += 1
                return

            for col in range(n):
                if col in cols or col + row in posDiag or col - row in negDiag:
                    continue
                
                placement = '.' * n
                placement = placement[:col] + 'Q' + placement[col + 1:]
                
                cols.add(col)
                posDiag.add(col + row)
                negDiag.add(col - row)

                backtrack(row + 1)

                cols.remove(col)
                posDiag.remove(col + row)
                negDiag.remove(col - row)

        backtrack(0)
        return res