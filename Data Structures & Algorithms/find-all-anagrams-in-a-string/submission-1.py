class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)

        window, pattern = [0] * 26, [0] * 26
        for ch in p:
            pattern[ord(ch) - ord('a')] += 1
        
        res, l = [], 0
        for r in range(n):           
            window[ord(s[r]) - ord('a')] += 1
            if r - l + 1 < m:
                continue
            
            if window == pattern:
                res.append(l)
            
            window[ord(s[l]) - ord('a')] -= 1
            l += 1

        return res