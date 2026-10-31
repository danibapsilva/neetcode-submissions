class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        res, stack = [0] * n, [] # (indx, temperature)
        for indx, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                stackIndx, _ = stack.pop()
                res[stackIndx] = indx - stackIndx
            stack.append((indx, temperature))
        
        return res