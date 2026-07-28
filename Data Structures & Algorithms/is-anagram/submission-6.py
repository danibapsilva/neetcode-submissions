class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        countS = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countS[t[i]] = countS.get(t[i], 0) - 1
        return set(countS.values()) == {0}