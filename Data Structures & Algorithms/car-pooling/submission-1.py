class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []
        for passengers, start, end in trips:
            points.append((start, passengers))
            points.append((end, -passengers))
        
        points.sort()
        currentCapacity = 0
        for _, passengers in points:
            currentCapacity += passengers
            if currentCapacity > capacity:
                return False
        return True
