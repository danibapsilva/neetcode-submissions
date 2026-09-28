class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, w = len(s1), len(s2), len(s3)
        if n + m != w:
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[-1][-1] = True

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i < n and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < m and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]

        # dp[i][j] represents if s1[i:] and s2[j:] can = s3[i + j:]
        # and the base case is going through both strings it their
        # entirety (n + 1 and m + 1), setting it to True.
        # we work backwards from the base case and we see wether s3
        # char can either be solved by taking from s1 (increment dp
        # [i + 1][j]) or taking from s2 (increment dp[i][j + 1]) and
        # if each subproblem allows the next iteration to see wether
        # furhter down the s3 string, we can solve more chars. So at
        # the end dp[0][0] represents wether we can solve the ENTIRE
        # s3 string, meaning s1[0:] and s2[0:] can interleave s3.