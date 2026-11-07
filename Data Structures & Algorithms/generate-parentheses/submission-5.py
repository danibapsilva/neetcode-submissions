class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def backtrack(opened: int, closed: int, curr: str) -> None:
            if opened == n == closed:
                res.append(curr)
                return
            
            if opened < n:
                backtrack(opened + 1, closed, curr + '(')
            if closed < opened:
                backtrack(opened, closed + 1, curr + ')')
        
        backtrack(0, 0, "")
        return res