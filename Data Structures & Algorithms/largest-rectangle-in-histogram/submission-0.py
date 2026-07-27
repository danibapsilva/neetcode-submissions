class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair height, index

        maxA = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                maxA = max(maxA, height * (i - index))
                start = index
            
            stack.append((h, start))
        
        # remaining
        for h, i in stack:
            maxA = max(maxA, h * (len(heights) - i))

        return maxA