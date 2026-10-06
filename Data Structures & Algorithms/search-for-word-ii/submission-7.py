class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        ROWS, COLS = len(board), len(board[0])

        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        res = set()
        def backtrack(r: int, c: int, node: TrieNode, curr: str):
            if (
                not 0 <= r < ROWS or
                not 0 <= c < COLS or
                board[r][c] not in node.children
            ):
                return
            
            ch = board[r][c]
            node = node.children[ch]
            if node.isWord:
                res.add(curr + ch)
            board[r][c] = '#'
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                backtrack(nr, nc, node, curr + ch)
            board[r][c] = ch


        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root, "")

        return list(res)