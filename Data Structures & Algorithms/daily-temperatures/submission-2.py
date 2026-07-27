class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [temp, indx]

        for i, num in enumerate(temperatures):
            while stack and stack[-1][0] < num:
                # res[stack[-1][1]] = i - stack[-1][1]
                # stack.pop()
                stackTemp, stackIndx = stack.pop()
                res[stackIndx] = i - stackIndx
            stack.append([num, i])
        
        return res