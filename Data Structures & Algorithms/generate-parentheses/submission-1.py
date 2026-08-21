class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, opened, closed):
            if opened == closed == n:
                res.append(curr)
                return
            
            if opened < n:
                curr += '('
                backtrack(curr, opened + 1, closed)
                curr = curr[:-1]
            
            if closed < opened:
                curr += ')'
                backtrack(curr, opened, closed + 1)
                curr = curr[:-1]

        backtrack("", 0, 0)  
        return res