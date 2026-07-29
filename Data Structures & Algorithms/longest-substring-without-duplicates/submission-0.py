class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        
        l = r = 0
        maxLen = 0
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen
