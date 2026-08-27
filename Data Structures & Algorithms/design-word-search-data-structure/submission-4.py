class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True

    def search(self, word: str) -> bool:
        
        def dfs(i, root):
            if i == len(word):
                return root.isWord

            ch = word[i]
            if ch == '.':
                for child in root.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            
            if ch not in root.children:
                return False
            
            return dfs(i + 1, root.children[ch])

        return dfs(0, self.root)
