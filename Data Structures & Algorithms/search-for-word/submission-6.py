class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(board), len(board[0])
        n = len(word)
        
        def backtrack(r: int, c: int, i: int) -> bool:
            if i == n:
                return True
            if (
                not 0 <= r < ROWS or
                not 0 <= c < COLS or
                board[r][c] != word[i]
            ):
                return False
            
            board[r][c] = '#'
            found = False
            for dr, dc in DIRECTIONS:
                nr, nc = dr + r, dc + c
                found = backtrack(nr, nc, i + 1) or found
            board[r][c] = word[i]
            
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        
        return False