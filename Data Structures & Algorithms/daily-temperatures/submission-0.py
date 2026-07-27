class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            counter = 0

            if i == len(temperatures) - 1:
                res.append(0)
                continue
            for j in range(i + 1, len(temperatures)):
                counter += 1
                if temperatures[j] > temperatures[i]:
                    res.append(counter)
                    break
                if j == len(temperatures) - 1:
                    res.append(0)

        
        return res