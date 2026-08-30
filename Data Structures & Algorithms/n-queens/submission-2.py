class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posDiags, negDiags = set(), set(), set()

        res, positions = [], []
        def backtrack(row: int) -> None:
            if row == n:
                res.append(positions.copy())
                return
            
            for col in range(n):
                if col in cols or row + col in posDiags or row - col in negDiags:
                    continue
                
                placement = '.' * n
                placement = placement[:col] + 'Q' + placement[col + 1:]

                cols.add(col)
                posDiags.add(row + col)
                negDiags.add(row - col)
                positions.append(placement)

                backtrack(row + 1)

                cols.remove(col)
                posDiags.remove(row + col)
                negDiags.remove(row - col)
                positions.pop()
        
        backtrack(0)
        return res
