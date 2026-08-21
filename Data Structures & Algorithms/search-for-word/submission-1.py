class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, ROWS, COLS = len(word), len(board), len(board[0])

        def backtrack(i, row, col):
            if i == n:
                return True
            
            if (
                min(row, col) < 0
                or row >= ROWS
                or col >= COLS
                or word[i] != board[row][col]
            ):
                return False

            board[row][col] = '#'
            found = (
                   backtrack(i + 1, row + 1, col)
                or backtrack(i + 1, row - 1, col)
                or backtrack(i + 1, row, col + 1)
                or backtrack(i + 1, row, col - 1)
            )
            board[row][col] = word[i]
            return found


        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(0, row, col):
                    return True
        return False