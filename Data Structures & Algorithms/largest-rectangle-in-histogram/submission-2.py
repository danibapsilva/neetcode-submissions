class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (indx, height)

        maxA = 0
        for i, h in enumerate(heights):

            start = i
            while stack and stack[-1][1] > h:
                indx, height = stack.pop()
                start = indx
                maxA = max(maxA, (i - indx) * height)
            stack.append((start, h))
        
        for indx, height in stack:
            maxA = max(maxA, (len(heights) - indx) * height)
        
        return maxA
