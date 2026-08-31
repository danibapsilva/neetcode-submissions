class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, indx)

        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                temperaturem, indx = stack.pop()
                res[indx] = i - indx
            stack.append((temp, i))
        return res