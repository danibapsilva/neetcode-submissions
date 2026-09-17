class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        dp = [False] * (n + 1)
        dp[-1] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                m = len(word)
                if i + m <= n and s[i: i + m] == word:
                    dp[i] = dp[i + m] # dp[i] relies on prior solved word break i + w
                if dp[i]:
                    break # found a valid solution, dont incorrectly override it
        return dp[0]


        # dp[i] represents wether we can break the whole string 's' at index 'i'
        # At the end of the word/len s + 1, we know it can be broken since there
        # is nothing left, so it can succesfully be broken indeed
        # and we work backwards from that point, with valid bounds checks and
        # checking wether at the current index, if we add a word from the dictionary
        # does it match? if yes we set dp[i], i being current index, to True, so when
        # we move backwards and find another match that ends at another dp[i] index
        # if the next dp[i] index is True, it means we were already able to solve the
        # prior subproblem. NOTE: dp[i] can ONLY be true if at the end of adding a
        # valid word break, we end at a dp[i] that is ALSO True.