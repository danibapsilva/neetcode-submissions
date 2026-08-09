class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        flips = 0

        for i in range(n):
            expected = '0' if i % 2 == 0 else '1'
            if s[i] != expected:
                flips += 1
        
        return min(flips, n - flips)