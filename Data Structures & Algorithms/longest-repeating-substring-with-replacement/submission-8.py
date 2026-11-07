class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        window = defaultdict(int)
        maxL = l = 0
        for r in range(n):
            window[s[r]] += 1
            while (r - l + 1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            maxL = max(maxL, r - l + 1)
        return maxL
            