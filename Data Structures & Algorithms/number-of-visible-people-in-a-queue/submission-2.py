class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n

        stack = [] # (indx, height)
        for i, h in enumerate(heights):
            
            while stack and stack[-1][1] < h:
                indx, height = stack.pop()
                answer[indx] += 1
            
            if stack and stack[-1][1] > h:
                answer[stack[-1][0]] += 1
            stack.append((i, h))
        
        # for i in range(n - 1):
        #     indx, height = stack[i]
        #     answer[indx] += 1

        return answer