class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)

        l = res = 0
        for r in range(1, n):
            if colors[l] == colors[r]:
                res += min(neededTime[l], neededTime[r])
                if neededTime[l] < neededTime[r]:
                    l = r
            else:
                l = r

        return res