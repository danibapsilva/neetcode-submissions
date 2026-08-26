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
            curr = root
            if i == len(word):
                return curr.isWord
            
            ch = word[i]
            if ch == '.':
                for child in curr.children.values():
                    if dfs(i + 1, child):
                        return True
            else:
                if ch not in curr.children:
                    return False
                return dfs(i + 1, curr.children[ch]) 

            return False
        

        return dfs(0, self.root)
