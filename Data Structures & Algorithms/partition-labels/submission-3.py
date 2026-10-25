class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for indx, ch in enumerate(s):
            lastIndex[ch] = indx
        
        size = end = 0
        res = []
        for indx, ch in enumerate(s):
            size += 1
            end = max(end, lastIndex[ch])

            if indx == end:
                res.append(size)
                size = 0
        return res