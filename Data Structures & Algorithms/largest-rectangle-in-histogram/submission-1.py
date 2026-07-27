class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (indx, height)

        maxA = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                indx, height = stack.pop()
                maxA = max(maxA, height * (i - indx))
                start = indx
            stack.append((start, h))
        
        # remaining
        for i, h in stack:
            maxA = max(maxA, h * (len(heights) - i))
        
        return maxA