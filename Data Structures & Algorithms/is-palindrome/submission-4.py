class Solution:
    def isPalindrome(self, s: str) -> bool:
        sClean = "".join([ch.lower() for ch in s if ch.isalnum()])
        # print(sClean)
        # for i in range(len(sClean)):
        #     left, right = i, len(sClean) - 1 - i
        #     if sClean[left] != sClean[right]:
        #         return False
        # return True
        return sClean == sClean[::-1]
            