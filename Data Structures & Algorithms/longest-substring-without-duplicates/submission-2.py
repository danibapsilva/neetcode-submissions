class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        window = set()
        
        maxL = l = 0
        for r in range(n):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            maxL = max(maxL, r - l + 1)
        return maxL
