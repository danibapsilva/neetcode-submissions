class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        maxL = 1
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while ((r - l + 1) - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            
            maxL = max(maxL, (r - l + 1))
        # while r < len(s):
        #     count[s[r]] = count.get(s[r], 0) + 1
        #     while ((r - l + 1) - max(count.values())) > k:
        #         count[s[l]] -= 1
        #         l += 1
            
        #     maxL = max(maxL, (r - l + 1))
        #     r += 1
        
        return maxL
        