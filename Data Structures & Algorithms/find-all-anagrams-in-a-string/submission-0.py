class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)

        window, pattern = defaultdict(int), defaultdict(int)
        for ch in p:
            pattern[ch] += 1
        
        res, l = [], 0
        for r in range(n):            
            window[s[r]] += 1
            if r - l + 1 < m:
                continue
            
            if window == pattern:
                res.append(l)
            
            window[s[l]] -= 1
            if not window[s[l]]:
                del window[s[l]]
            l += 1

        return res