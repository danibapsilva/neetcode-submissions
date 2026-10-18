class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIGIT_TO_CHARS = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': 'tuv',
            '9': 'wxyz'
        }

        n, res = len(digits), []
        def backtrack(i: int, curr: str) -> None:
            if len(curr) == n:
                res.append(curr)
                return
            
            for ch in DIGIT_TO_CHARS[digits[i]]:
                backtrack(i + 1, curr + ch)
        
        if digits:
            backtrack(0, "")
        
        return res