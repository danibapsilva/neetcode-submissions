class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, positions = [], []

        def backtrack(queens):
            if queens == n:
                res.append(positions.copy())
                return

            for col in range(n):
                if self.canPlace(positions, queens, col): # row to place is # of curr queens
                    placement = '.' * n
                    placement = placement[:col] + 'Q' + placement[col + 1:]
                    
                    positions.append(placement)
                    backtrack(queens + 1)
                    positions.pop()
        
        backtrack(0)
        return res
    
    def canPlace(self, positions: List[str], r: int, c: int) -> bool:
        n = len(positions)
        for row in range(n): # Same row check handled by iteration
            if positions[row][c] == 'Q': # Same column check
                return False
            
            m = len(positions[row])
            diff = r - row
            if (
                   (c + diff < m and positions[row][c + diff] == 'Q') # pos diag
                or (c - diff >= 0 and positions[row][c - diff] == 'Q') # neg diag
            ): # Bi-directional same diagonal check
                return False
        return True

                