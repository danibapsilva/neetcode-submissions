class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        if max(freq) > (n + 1) // 2:
            return ""
        
        maxHeap = [] # (-count, char)
        for indx, cnt in enumerate(freq):
            if cnt:
                heapq.heappush(maxHeap, [-cnt, chr(indx + ord('a'))])
        
        prev, res = None, ""
        while prev or maxHeap:
            if prev and not maxHeap:
                return ""
            
            cnt, ch = heapq.heappop(maxHeap)
            cnt, res = cnt + 1, res + ch

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt: # important to not add chars with no count remaining
                prev = [cnt, ch]
        
        return res
