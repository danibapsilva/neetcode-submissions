class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for num in stones:
            heapq.heappush(heap, -num)
        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)

            if x > y:
                heapq.heappush(heap, -(x - y))
        
        return -heap[0] if heap else 0
            