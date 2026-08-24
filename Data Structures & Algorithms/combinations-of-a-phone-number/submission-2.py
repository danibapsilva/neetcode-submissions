class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, combination = [], ""

        DIGIT_TO_CHARS = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        def backtrack(i):
            nonlocal combination

            if i == len(digits):
                res.append(combination)
                return

            for ch in DIGIT_TO_CHARS[digits[i]]:
                combination += ch
                backtrack(i + 1)
                combination = combination[:-1]           
        
        if digits:
            backtrack(0)
        return res
