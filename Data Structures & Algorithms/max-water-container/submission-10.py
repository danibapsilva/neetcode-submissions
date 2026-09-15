class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        maxA = 0
        l, r = 0, n - 1
        while l < r:
            maxA = max(maxA, (r - l) * min(heights[l], heights[r]))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxA