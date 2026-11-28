class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        
        heap, currentCapacity = [], 0
        for passengers, start, end in trips:
            while heap and heap[0][0] <= start:
                _, passengersDropped = heapq.heappop(heap)
                currentCapacity -= passengersDropped

            heapq.heappush(heap, (end, passengers))
            currentCapacity += passengers
            if currentCapacity > capacity:
                return False
        
        return True