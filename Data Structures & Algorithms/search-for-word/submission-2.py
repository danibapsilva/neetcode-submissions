class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, ROWS, COLS = len(word), len(board), len(board[0])
        
        def backtrack(row, col, i):
            if i == n:
                return True
            
            if (
                min(row, col) < 0
                or row >= ROWS
                or col >= COLS
                or board[row][col] != word[i]
            ):
                return False
            
            board[row][col] = '#'
            found = (
                backtrack(row + 1, col, i + 1)
                or backtrack(row - 1, col, i + 1)
                or backtrack(row, col + 1, i + 1)
                or backtrack(row, col - 1, i + 1)
            )
            board[row][col] = word[i]
            
            return found
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        
        return False