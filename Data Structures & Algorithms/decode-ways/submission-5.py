class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        one, two = 1, 0
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                curr = 0 
            else:
                curr = one
                if i + 1 < n and 10 <= int(s[i: i + 2]) <= 26:
                    curr += two
            
            one, two = curr, one

        return one