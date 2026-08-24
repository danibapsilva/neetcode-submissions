class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)

            smashed = abs(x - y)
            if smashed:
                heapq.heappush(heap, -smashed)
        return -heap[0] if heap else 0