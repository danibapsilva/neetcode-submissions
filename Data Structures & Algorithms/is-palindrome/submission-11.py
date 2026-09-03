class Solution:
    def isPalindrome(self, s: str) -> bool:
        sClean = "".join([ch.lower() for ch in s if ch.isalnum()])
        n = len(sClean)

        r = n - 1
        for l in range(n):
            if sClean[l] != sClean[r]:
                return False
            r -= 1
        return True