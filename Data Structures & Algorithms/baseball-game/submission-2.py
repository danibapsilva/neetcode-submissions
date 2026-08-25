class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        res = 0
        for op in operations:
            if op == '+':
                entry = stack[-1] + stack[-2]
                res += entry
                stack.append(entry)
            elif op == 'D':
                entry = stack[-1] * 2
                res += entry
                stack.append(entry)
            elif op == 'C':
                res -= stack.pop()
            else:
                entry = int(op)
                res += entry
                stack.append(entry)
        
        return res