class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch not in match:
                stack.append(ch)
            elif stack and stack[-1] == match[ch]:
                stack.pop()
            else:
                return False
            

        return True if not stack else False
                