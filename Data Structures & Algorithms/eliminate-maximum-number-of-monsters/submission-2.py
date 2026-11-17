class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        for dst, spd in zip(dist, speed):
            time = dst / spd
            heapq.heappush(heap, time)
        
        eliminated = 0
        while heap:
            time = heapq.heappop(heap)
            if eliminated >= time:
                return eliminated
            eliminated += 1
        return eliminated

