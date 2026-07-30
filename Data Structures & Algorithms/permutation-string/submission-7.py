class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0] * 26
        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1

        l = 0
        r = len(s1) - 1
        while r < len(s2):
            freq2 = [0] * 26
            for i in range(l, r + 1):
                if s2[i] in s1:
                    freq2[ord(s2[i]) - ord('a')] += 1

                    if freq2[ord(s2[i]) - ord('a')] > freq1[ord(s2[i]) - ord('a')]:
                        break
                    if freq1 == freq2:
                        return True
                else:
                    break
            l += 1
            r += 1

        return False
