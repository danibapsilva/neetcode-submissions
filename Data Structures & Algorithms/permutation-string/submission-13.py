class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        freq1 = [0] * 26
        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1
        
        freq2 = [0] * 26
        l = 0
        for r in range(m):
            freq2[ord(s2[r]) - ord('a')] += 1
            if (r - l) + 1 == n:
                if freq1 == freq2:
                    return True
                freq2[ord(s2[l]) - ord('a')] -= 1
                l += 1

        return False