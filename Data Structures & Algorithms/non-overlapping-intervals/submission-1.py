class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)

        removes = 0
        prevEnd = intervals[0][1]
        for i in range(1, n):
            start, end = intervals[i]
            
            if prevEnd > start:
                removes += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        return removes