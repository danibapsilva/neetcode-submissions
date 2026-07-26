class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch not in match: # is opener
                stack.append(ch)
            elif match[ch] not in stack:
                return False
            elif stack and match[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return True if not stack else False