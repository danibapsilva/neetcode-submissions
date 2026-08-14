class Solution:
    def maxDepth(self, s: str) -> int:
        maxL = curr = 0
        for ch in s:
            if ch == '(':
                curr += 1
            elif ch == ')':
                curr -= 1
            maxL = max(maxL, curr)
        
        return maxL