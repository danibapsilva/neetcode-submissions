class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)

        mpTS, mpST = {}, {}
        for i in range(n):
            ch1, ch2 = s[i], t[i]
            if (
                ch1 in mpST and mpST[ch1] != ch2 or
                ch2 in mpTS and mpTS[ch2] != ch1
            ):
                return False
            mpST[ch1] = ch2
            mpTS[ch2] = ch1
        return True