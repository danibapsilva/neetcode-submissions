class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freqs = defaultdict(int)
        for word in words:
            for ch in word:
                freqs[ch] += 1
        
        for ch in freqs:
            if freqs[ch] % len(words):
                return False
        
        return True