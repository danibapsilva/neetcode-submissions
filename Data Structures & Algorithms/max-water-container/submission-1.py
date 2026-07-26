class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        for i in range(len(heights)):
            # print(i)
            for j in range(i + 1, len(heights)):
                width = j - i
                height = min(heights[i], heights[j])
                if width * height > maxA:
                    maxA = width * height
        
        return maxA