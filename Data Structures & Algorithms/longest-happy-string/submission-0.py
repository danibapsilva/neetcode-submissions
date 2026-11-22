class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = [] # (occurances, letter)
        
        for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count:
                heapq.heappush(maxHeap, (-count, char))
        
        res = ""
        while maxHeap:
            n = len(res)
            count, char = heapq.heappop(maxHeap)
            if n >= 2 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                happyCount, happyChar = heapq.heappop(maxHeap)
                res += happyChar
                
                happyCount += 1 # plus means decrease in maxHeap

                if happyCount: # if used all occurances
                    heapq.heappush(maxHeap, (happyCount, happyChar))
            else:
                res += char
                count += 1 # plus means decrease in maxHeap
            
            if count: # if used all occurances
                heapq.heappush(maxHeap, (count, char))
        return res
