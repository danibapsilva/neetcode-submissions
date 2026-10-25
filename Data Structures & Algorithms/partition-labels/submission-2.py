class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)

        last = {}
        for indx, ch in enumerate(s):
            last[ch] = indx
        
        l = r = 0
        res = []
        while r < n:
            r = last[s[r]]
            i = l
            while i <= r:
                r = max(r, last[s[i]])
                i += 1
            res.append(r - l + 1)
            r += 1
            l = r
        return res