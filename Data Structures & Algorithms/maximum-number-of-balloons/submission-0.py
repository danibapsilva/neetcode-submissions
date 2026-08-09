class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq1 = [0] * 26
        for ch in "balloon":
            freq1[ord(ch) - ord('a')] += 1
        
        freq2 = [0] * 26
        for ch in text:
            freq2[ord(ch) - ord('a')] += 1
        
        ans = float('inf')
        for i in range(len(freq1)):
            if freq1[i] > 0:
                ans = min(ans, freq2[i] // freq1[i])
        
        return ans

