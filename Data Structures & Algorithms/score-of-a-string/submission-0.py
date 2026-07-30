class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0

        i = 0
        while i < len(s) - 1:
            diff = abs(ord(s[i]) - ord(s[i + 1]))
            total += diff
            i += 1
        
        return total
