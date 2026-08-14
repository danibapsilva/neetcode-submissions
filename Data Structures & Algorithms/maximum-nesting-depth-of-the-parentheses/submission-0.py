class Solution:
    def maxDepth(self, s: str) -> int:
        match = {')': '(', '[': ']', '}': '{'}
        stack = []

        maxL = 0
        for ch in s:
            if ch in match.values():
                stack.append(ch)
            elif ch in match:
                stack.pop()
            maxL = max(maxL, len(stack))
        
        return maxL