class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, ROWS, COLS = len(words), len(board), len(board[0])
        
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        res = set()
        def backtrack(row, col, node, word):
            if (
                min(row, col) < 0
                or row >= ROWS or col >= COLS
                or board[row][col] not in node.children
            ):
                return

            
            ch = board[row][col]
            node = node.children[ch]
            word += ch
            board[row][col] = '#'
            if node.isWord:
                res.add(word)

            backtrack(row + 1, col, node, word)
            backtrack(row - 1, col, node, word)
            backtrack(row, col + 1, node, word)
            backtrack(row, col - 1, node, word)
            board[row][col] = ch

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root, "")
        
        return list(res)