class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        answer = []

        for i in range(len(heights)):
            currMax = 0
            count = 0
            for j in range(i + 1, len(heights)):
                if heights[j] > currMax:
                    if heights[i] > currMax:
                        count += 1
                    currMax = heights[j]
            
            answer.append(count)

        return answer