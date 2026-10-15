class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        
        res = []
        for i in range(n):
            start, end = intervals[i][0], intervals[i][1]
            newStart, newEnd = newInterval
            if newEnd < start:
                res.append([newStart, newEnd])
                return res + intervals[i:]
            elif newStart <= end:
                mergedStart, mergedEnd = min(start, newStart), max(end, newEnd)
                newInterval = [mergedStart, mergedEnd]
            else:
                res.append([start, end])

        res.append(newInterval)
        return res