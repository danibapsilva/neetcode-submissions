class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxL = ""
        for i in range(len(s)):
            max1 = self.countPalindromes(i, i, s)
            max2 = self.countPalindromes(i, i + 1, s)

            maxL = max(maxL, max1, max2, key=len)
        return maxL
    
    def countPalindromes(self, l: int, r: int, s: str) -> str:
        maxL = ""
        while l >= 0 and r < len(s) and s[l] == s[r]:
            maxL = s[l: r + 1] if (r - l) + 1 > len(maxL) else maxL
            l -= 1
            r += 1
        
        return maxL
