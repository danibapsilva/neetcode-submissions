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

        # at the core of the recursive logic, we simply just memoize
        # the possibilities of forming t[j:] with s[i:] in dp, and then
        # we consider the possbility of skipping/excluding the current
        # character, dfs(i + 1, j), or if s[i] == t[j], we can consider
        # the possibility of adding/including the current character,
        # dfs(i + 1, j + 1).
