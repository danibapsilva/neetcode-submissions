class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        if len(self.small) > len(self.large) + 1:
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        elif len(self.large) > len(self.small) + 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            median = -self.small[0]
            return median
        elif len(self.large) > len(self.small):
            median = self.large[0]
            return median
        else:
            smallMax = -self.small[0]
            largeMin = self.large[0]
            median = (smallMax + largeMin) / 2.0
            return median
        
        