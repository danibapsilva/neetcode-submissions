class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while k > 0 and stack and stack[-1] > ch:
                k -= 1
                stack.pop()
            stack.append(ch)
        
        while stack and k:
            k -= 1
            stack.pop()
        
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        
        res = stack[i:]
        return ''.join(res) if res else '0'