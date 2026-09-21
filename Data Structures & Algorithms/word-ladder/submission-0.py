class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        words, res = set(wordList), 0
        q = deque([beginWord])
        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return res
                
                for i in range(len(node)):
                    for ch in range(ord('a'), ord('z') + 1):
                        ch = chr(ch)
                        if node[i] == ch:
                            continue
                        nei = node[:i] + ch + node[i + 1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        
        return 0