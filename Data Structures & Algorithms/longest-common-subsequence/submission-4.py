class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]

        # dp[i][j] represents the LCS from text1[i:] and text2[j:]
        # we set all initial LCA positions values to a base case of 0 and add an
        # extra column and row for out of bounds safety/base, and then we start
        # the bottom-up approach by start at the bottom-right corner. At each
        # cell we check wether the current char of text1 and text2 is equal
        # if it is we want to move both pointers up one/look at the remaining and set
        # dp[i][j] to be i + the prior diagonal bottom-right since always larger than
        # the bottom/downwards cell and right/forwards cell,
        # but if they are not equal, we want to set the current LCA of the position
        # to be the max amount of moving forward with text1 (move right one cell),
        # and the amount of moving downward with text2 (move down one cell)
