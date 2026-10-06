class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if m > n:
            return 0

        dp = {}
        def dfs(i: int, j: int) -> int:
            if j == m:
                return 1
            if i == n:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            dp[(i, j)] = res
            return res

        return dfs(0, 0)
