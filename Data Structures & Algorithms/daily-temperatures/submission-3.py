class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, indx)

        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                temp, indx = stack.pop()
                res[indx] = i - indx
            stack.append((temperature, i))
        
        return res