class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        
        wordSet, res = set(wordList), 0
        q = deque([beginWord])
        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res
    
                for i in range(len(node)):
                    for code in range(ord('a'), ord('z') + 1):
                        ch = chr(code)
                        if node[i] == ch:
                            continue
                        nei = node[:i] + ch + node[i + 1:]
                        if nei in wordSet:
                            q.append(nei)
                            wordSet.remove(nei)
        return 0
