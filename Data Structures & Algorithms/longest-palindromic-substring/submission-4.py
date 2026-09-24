class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        maxL = ""
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    maxL = max(maxL, s[i: j + 1], key=len)
        return maxL

        # dp[i][j] represents if s[i: j + 1] is a palindrome
        # we work backwards and initialize every substring to be False, invalid,
        # and we then check every substring from i -> end of string, if we find any
        # valid palindromes. a valid palindrome defined as left and right pointers,
        # i and j correspondingly, must also be either <= len 3, or if we already
        # solved the prior subproblem (if we move each pointer 1 position inward),
        # if that is True/is indeed a palindrome, we know this know string is also
        # indeed a palindrome, after each new palindrome that we find, we update
        # a global maxL and return that maxL after trying all substrings
