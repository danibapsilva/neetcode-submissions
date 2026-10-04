class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        freq1 = [0] * 26
        for ch in s:
            freq1[ord(ch) - ord('a')] += 1
        freq2 = [0] * 26
        for ch in t:
            freq2[ord(ch) - ord('a')] += 1
        return freq1 == freq2