class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        for ch in s1:
            freq1[ord(ch) - ord('a')] = freq1.get(ord(ch) - ord('a'), 0) + 1
        
        l = 0
        r = len(s1) - 1
        freq2 = {}
        for r in range(len(s2)):
            freq2[ord(s2[r]) - ord('a')] = freq2.get(ord(s2[r]) - ord('a'), 0) + 1

            if freq1 == freq2:
                return True
            # elif freq2[ord(s2[r]) - ord('a')] > freq1.get(ord(s2[r]) - ord('a'), 0):
            #     continue
            
            if (r - l + 1) == len(s1):
                freq2[ord(s2[l]) - ord('a')] -= 1
                if freq2[ord(s2[l]) - ord('a')] == 0:
                    del freq2[ord(s2[l]) - ord('a')]
                l += 1

                
            

        return False
