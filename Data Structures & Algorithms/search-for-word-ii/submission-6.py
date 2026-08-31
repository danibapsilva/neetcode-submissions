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
        def backtrack(r: int, c: int, node: TrieNode, word: str) -> None:
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or board[r][c] not in node.children
            ):
                return
            
            ch = board[r][c]
            node = node.children[ch]
            word += ch
            if node.isWord:
                res.add(word)
            board[r][c] = '#'

            for dr, dc in DIRECTIONS:
                backtrack(r + dr, c + dc, node, word)
            board[r][c] = ch
            

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root, "")
            
        return list(res)