class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        stack = [intervals[0]]
        for startTime, endTime in intervals:
            lastStart, lastEnd = stack[-1]
            if startTime <= lastEnd:
                stack[-1] = [lastStart, max(endTime, lastEnd)]
            else:
                stack.append([startTime, endTime])
        
        return stack