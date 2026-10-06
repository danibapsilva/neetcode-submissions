class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = defaultdict(int)
        
        l = maxL = 0
        for r in range(n):
            freq[s[r]] += 1
            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            maxL = max(maxL, r - l + 1)
        return maxL