class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', ']':'[', '}': '{'}
        
        stack = []
        for ch in s:
            if ch not in match:
                stack.append(ch)
            elif not stack or match[ch] != stack[-1]:
                return False
            else:
                stack.pop()
        
        return len(stack) == 0
            
                