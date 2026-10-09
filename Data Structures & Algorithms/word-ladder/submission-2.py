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

        # We initially check if endWord is even a possible node or if beginWord is
        # already the endWord solution, if not we start the actual algorithm.
        # we treat the beginWord as the starting graph node and run a bfs, each layer
        # or ring, counts for one res increment since these would all be searching in
        # parallel. We look at q and check every node in the q, every node is a word/
        # We look at every char in the word/node, check every letter in the alphabet,
        # and see wether if we subsitute a letter in word, if it exists, we call that
        # a neighbor and we subsquently remove it from the wordList/set of
        # possibilites to mark it as visited from set, and then add the neighbor
        # possibility to the q for the next layer of bfs.