class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n

        stack = [] # indx
        for i, h in enumerate(heights):

            while stack and heights[stack[-1]] < h:
                answer[stack.pop()] += 1
            
            if stack: # all smaller popped
                answer[stack[-1]] += 1

            stack.append(i)

        return answer