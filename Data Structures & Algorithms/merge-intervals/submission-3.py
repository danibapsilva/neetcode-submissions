class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        stack = [intervals[0]]
        for start, end in intervals:
            lastStart, lastEnd = stack[-1][0], stack[-1][1]
            if stack and start <= lastEnd:
                stack[-1] = [lastStart, max(end, lastEnd)]
            else:
                stack.append([start, end])
        return stack

            