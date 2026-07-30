class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = list(s[::-1])

        for i in range(len(t)):
            if stack and stack[-1] == t[i]:
                stack.pop()

        return len(stack) == 0