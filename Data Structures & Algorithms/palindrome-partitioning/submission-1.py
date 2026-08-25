class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n, res, partition = len(s), [], []

        def backtrack(start):
            if start == n:
                res.append(partition.copy())
                return
            
            for child in range(start, n):
                if self.isPalindrome(s, start, child):
                    partition.append(s[start: child + 1])
                    backtrack(child + 1)
                    partition.pop()
        
        backtrack(0)
        return res

            
                 
    
    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True