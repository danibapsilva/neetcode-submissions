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
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        root = TrieNode()
        for word in strs:
            root.addWord(word)
        
        curr = root
        prefix = ""
        while len(curr.children) == 1 and not curr.isWord:
            ch = list(curr.children)[0]
            prefix += ch
            curr = curr.children[ch]

        return prefix