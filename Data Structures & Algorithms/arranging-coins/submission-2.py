class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        res = 0
        i = 1
        while n > 0:

            n -= i
            if n >= 0:
                res += 1
            
            i += 1
             

        return res