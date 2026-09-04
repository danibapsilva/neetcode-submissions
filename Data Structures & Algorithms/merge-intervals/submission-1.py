class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        stack = [intervals[0]]

        for startTime, endTime in intervals:
            if startTime <= stack[-1][1]:
                stack[-1] = [stack[-1][0], max(stack[-1][1], endTime)]
            else:
                stack.append([startTime, endTime])
        return stack