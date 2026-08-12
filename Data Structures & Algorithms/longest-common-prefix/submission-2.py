class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs[0]) == 0:
            return ""
    
        maxP = strs[0][0]

        while True:
            for indx, s in enumerate(strs):
                m = len(maxP)
                if len(s) < m:
                    return maxP[:len(s)]
                
                if s[:m] != maxP:
                    maxP = maxP[:-1]
                    return maxP
                if indx == len(strs) - 1: # last element
                    if len(s) == m:
                        return maxP
                    maxP += s[m]
