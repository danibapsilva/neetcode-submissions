class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            stone1, stone2 = heapq.heappop(heap), heapq.heappop(heap)
            if not stone1 == stone2:
                heapq.heappush(heap, -abs(stone1 - stone2))
        
        return -heap[0] if heap else 0