class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        n, m = len(s), len(t)
        if n != m:
            return False
        for i in range(n):
            freq[s[i]] += 1
            freq[t[i]] -= 1
        return set(freq.values()) == {0}