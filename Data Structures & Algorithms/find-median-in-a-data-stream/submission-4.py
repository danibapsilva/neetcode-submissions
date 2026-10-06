class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        s, l = len(self.small), len(self.large)
        if s > l + 1:
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        elif l > s + 1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)

    def findMedian(self) -> float:
        s, l = len(self.small), len(self.large)
        if (s + l) % 2:
            return -self.small[0] if s > l else self.large[0]
        return (-self.small[0] + self.large[0]) / 2.0
        
        