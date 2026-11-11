class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, m = len(a), len(b)
        i, j = n - 1, m - 1

        res, carry = [], 0
        while i >= 0 or j >= 0 or carry:
            iVal, jVal = int(a[i]) if i >= 0 else 0, int(b[j]) if j >= 0 else 0
            
            total = iVal ^ jVal ^ carry
            if iVal + jVal + carry >= 2:
                carry = 1
            else:
                carry = 0
            
            res.append(str(total))
            i, j = i - 1, j - 1
        
        return "".join(res)[::-1]
