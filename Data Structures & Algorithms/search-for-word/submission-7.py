class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(board), len(board[0])
        
        def backtrack(i: int, r: int, c: int) -> bool:
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
                found = found or backtrack(i + 1, nr, nc)
            board[r][c] = word[i]
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(0, r, c):
                    return True
        return False