class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', ']': '[', '}': '{'}

        stack = []
        for ch in s:
            if ch not in match:
                stack.append(ch)
            elif not stack or stack[-1] != match[ch]:
                return False
            else:
                stack.pop()
        
        return not len(stack)