class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        stack = [intervals[0]]
        for start, end in intervals:
            prevStart, prevEnd = stack[-1][0], stack[-1][1]
            if stack and start <= prevEnd:
                mergedEnd = max(prevEnd, end)
                stack[-1] = [prevStart, mergedEnd]
            else:
                stack.append([start, end])
        return stack
                