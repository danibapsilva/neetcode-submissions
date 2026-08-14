class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []

        maxL = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                stack.pop()
            maxL = max(maxL, len(stack))
        
        return maxL