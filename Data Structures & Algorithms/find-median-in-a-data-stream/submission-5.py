class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        n, m = len(self.small), len(self.large)
        if n > m + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -val)
        elif m > n + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        n, m = len(self.small), len(self.large)
        if (n + m) % 2:
            return -self.small[0] if n > m else self.large[0]
        return (-self.small[0] + self.large[0]) / 2.0
        