class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        n = len(s)
        def backtrack(i):
            if i == n:
                res.append(part.copy())
                return
            
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    part.append(s[i: j + 1])
                    backtrack(j + 1)
                    part.pop()
        
        backtrack(0)
        return res
    
    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
