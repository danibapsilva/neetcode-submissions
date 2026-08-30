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
        n = len(digits)

        res, combination = [], ""
        def backtrack(start: int) -> None:
            nonlocal combination

            if start == n:
                res.append(combination)
                return
            
            for ch in DIGIT_TO_CHARS[digits[start]]:
                combination += ch
                backtrack(start + 1)
                combination = combination[:-1]
        
        if digits:
            backtrack(0)
        return res
