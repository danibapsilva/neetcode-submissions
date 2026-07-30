class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0] * 26
        for ch in s1:
            idx = ord(ch) - ord('a')
            freq1[idx] += 1

        l = 0
        freq2 = [0] * 26

        for r in range(len(s2)):
            idx = ord(s2[r]) - ord('a')
            freq2[idx] += 1

            if (r - l + 1) == len(s1):
                if freq1 == freq2:
                    return True

                idx = ord(s2[l]) - ord('a')
                freq2[idx] -= 1
                l += 1

        return False